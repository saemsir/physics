"""Convert local PDF files to page-preserving Markdown."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

try:
    import pymupdf
except ImportError:
    try:
        import fitz as pymupdf
    except ImportError as exc:
        raise SystemExit(
            "PDF conversion requires PyMuPDF; install project dependencies with "
            "`python -m pip install -r requirements.txt`."
        ) from exc


ROOT = Path(__file__).resolve().parent
DEFAULT_DIRS = (ROOT / "exam_papers", ROOT / "book")


def _markdown_for_pdf(path: Path) -> tuple[str, int, int]:
    try:
        document = pymupdf.open(path)
    except (OSError, RuntimeError) as exc:
        raise ValueError(f"cannot open PDF: {exc}") from exc

    sections: list[str] = [
        f"# {path.stem}\n",
        f"> Source: `{path.name}`  ",
        f"> Pages: {document.page_count}\n",
    ]
    text_pages = 0
    empty_pages: list[int] = []
    try:
        for number, page in enumerate(document, start=1):
            text = page.get_text("text").strip()
            sections.append(f"\n## Page {number}\n")
            if text:
                sections.append(text + "\n")
                text_pages += 1
            else:
                sections.append(
                    "> No embedded text extracted from this page; OCR or manual review is needed.\n"
                )
                empty_pages.append(number)
    finally:
        document.close()

    if empty_pages:
        page_list = ", ".join(map(str, empty_pages))
        sections.insert(
            3,
            f"> Pages requiring OCR/manual review: {page_list}  \n",
        )
    return "\n".join(sections).rstrip() + "\n", text_pages, len(empty_pages)


def convert(directories: tuple[Path, ...], *, overwrite: bool = False) -> int:
    pdfs = sorted(
        (path for directory in directories if directory.is_dir()
         for path in directory.rglob("*")
         if path.is_file() and path.suffix.casefold() == ".pdf"),
        key=lambda path: path.as_posix().casefold(),
    )
    if not pdfs:
        print("No PDFs found in the selected directories.", file=sys.stderr)
        return 1

    failures = 0
    for source in pdfs:
        target = source.with_suffix(".md")
        if target.exists() and not overwrite and target.stat().st_mtime >= source.stat().st_mtime:
            print(f"SKIP {source}: up-to-date")
            continue
        try:
            content, text_pages, empty_pages = _markdown_for_pdf(source)
            target.write_text(content, encoding="utf-8")
        except (OSError, ValueError, RuntimeError) as exc:
            failures += 1
            print(f"ERROR {source}: {exc}", file=sys.stderr)
            continue

        status = f"{text_pages} text pages"
        if empty_pages:
            status += f", {empty_pages} pages need OCR/manual review"
        print(f"WROTE {target}: {status}")

    print(f"Processed {len(pdfs)} PDFs; {failures} failed.")
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Extract each local PDF into a page-labelled .mmd file."
    )
    parser.add_argument(
        "--directories",
        nargs="+",
        type=Path,
        default=DEFAULT_DIRS,
        help="directories to scan recursively (default: exam_papers book)",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="replace existing .mmd files even when they are newer than the PDF",
    )
    args = parser.parse_args(argv)
    return convert(tuple(path.resolve() for path in args.directories), overwrite=args.overwrite)


if __name__ == "__main__":
    raise SystemExit(main())
