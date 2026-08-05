"""Fast, dependency-free checks for Hecate's public documentation boundary."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]

REQUIRED_FILES = (
    "README.md",
    "docs/BRANCHING.md",
    "docs/GITHUB_PLANNING.md",
    "docs/LOCAL_DATA_BOUNDARY.md",
    "vault/README.md",
    "vault/ROADMAP.md",
    ".github/ISSUE_TEMPLATE/feature.yml",
    ".github/ISSUE_TEMPLATE/bug.yml",
    ".github/ISSUE_TEMPLATE/research.yml",
    ".github/ISSUE_TEMPLATE/docs.yml",
    ".github/pull_request_template.md",
)

REQUIRED_PHRASES = {
    "README.md": ("pre-implementation stage",),
    "vault/README.md": (
        "untrusted reference material",
        "must remain outside the Obsidian-visible vault",
    ),
    "docs/GITHUB_PLANNING.md": ("never a home-data store",),
    "docs/LOCAL_DATA_BOUNDARY.md": (
        "<username>",
        "<distro>",
        "<projects-directory>",
    ),
}

PUBLIC_DATA_PATTERNS = {
    "credential-shaped token": re.compile(
        r"(?:gh[opusr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|"
        r"sk-[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{16}|eyJ[A-Za-z0-9_-]{20,}\.)"
    ),
    "resolved Windows user path": re.compile(
        r"[A-Za-z]:\\Users\\(?!<username>)", re.IGNORECASE
    ),
    "resolved WSL home path": re.compile(r"/home/(?!<username>)"),
    "resolved WSL distribution": re.compile(
        r"\\\\wsl\.localhost\\(?!<distro>)", re.IGNORECASE
    ),
    "assigned secret": re.compile(
        r"(?:password|token|api[_ -]?key|lock[_ -]?code)\s*[:=]\s*"
        r"[^<\s][^\r\n]*",
        re.IGNORECASE,
    ),
}

LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def github_slug(heading: str) -> str:
    heading = heading.strip().lower()
    heading = re.sub(r"<[^>]+>", "", heading)
    heading = re.sub(r"[^a-z0-9 _-]", "", heading)
    return re.sub(r"[ _]+", "-", heading)


def check_markdown(path: Path, errors: list[str]) -> None:
    relative = path.relative_to(ROOT).as_posix()
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        errors.append(f"{relative}: not valid UTF-8")
        return

    lines = text.splitlines()
    if relative != ".github/pull_request_template.md":
        h1_count = sum(line.startswith("# ") for line in lines)
        if h1_count != 1:
            errors.append(f"{relative}: expected exactly one H1, found {h1_count}")

    for number, line in enumerate(lines, start=1):
        if line.rstrip(" \t") != line:
            errors.append(f"{relative}:{number}: trailing whitespace")
        if "\t" in line:
            errors.append(f"{relative}:{number}: tab character")

    headings = {
        github_slug(match.group(1))
        for match in re.finditer(r"^#{1,6}\s+(.+)$", text, re.MULTILINE)
    }
    for match in LINK_PATTERN.finditer(text):
        raw_target = match.group(1).strip()
        if raw_target.startswith(("http://", "https://", "mailto:")):
            continue
        if raw_target.startswith("#"):
            if raw_target[1:] not in headings:
                errors.append(f"{relative}: missing heading {raw_target}")
            continue

        file_target = unquote(raw_target.split("#", 1)[0])
        resolved = (path.parent / file_target).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            errors.append(f"{relative}: link leaves repository: {raw_target}")
            continue
        if not resolved.exists():
            errors.append(f"{relative}: missing local link: {raw_target}")

    for label, pattern in PUBLIC_DATA_PATTERNS.items():
        if pattern.search(text):
            errors.append(f"{relative}: contains {label}")


def main() -> int:
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        if not (ROOT / relative).exists():
            errors.append(f"missing required file: {relative}")

    markdown_files = sorted(
        path for path in ROOT.rglob("*.md") if ".git" not in path.parts
    )
    for path in markdown_files:
        check_markdown(path, errors)

    for relative, phrases in REQUIRED_PHRASES.items():
        path = ROOT / relative
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{relative}: missing required policy text: {phrase}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"Documentation checks passed for {len(markdown_files)} Markdown files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
