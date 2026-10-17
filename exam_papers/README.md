# Exam-paper inputs

Put text-based exam papers in this folder. `convert_pdfs.py` creates
page-labelled `.md` text extractions from PDFs under `exam_papers/` and
`book/`; pages without embedded text are marked for OCR/manual review.
`matrix_pipeline.py` reads `.mmd`, `.md`, `.txt`, and `.docx` files recursively;
it splits questions at numbered lines
such as `Question 1.` or `Q2:`. If no numbered question headings are found,
the file is treated as one question. Keep source citations and usage rights
outside the question wording where appropriate.

The pipeline processes files locally. It does not copy question or book text
into its JSON output; it stores file paths, concept scores, and matrix data.
PDFs, scans, and images are not OCR'd and are reported as unsupported, so
convert them to reviewed text or DOCX before indexing. Detected concept links
are suggestions for human review, not verified exam tags or solutions.

Run from the repository root:

```bash
python matrix_pipeline.py
```

Use `--exam-papers`, `--books`, and `--output` to select other paths.
