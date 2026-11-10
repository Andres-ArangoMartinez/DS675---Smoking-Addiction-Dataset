# Shared LaTeX report

LaTeX is the official shared report source. Use `main.tex` for shared formatting.

## Writing workflow

1. **Choose a section** from the table below and coordinate one editor at a time for that file.
2. **Edit its text** in any text editor, keeping LaTeX commands intact. Use the comments as writing prompts and replace draft placeholders with agreed methods or verified findings.
3. **Request teammate review** of your changes using the [collaboration workflow](../CONTRIBUTING.md).

One teammate with LaTeX installed can compile and share the PDF for group review. Everyone can begin writing without installing LaTeX.

## What to edit

| File under `sections/` | Content to develop |
| --- | --- |
| `01_introduction.tex` | Precise supervised task, motivation, and intended extension beyond Kaggle work |
| `02_data.tex` | Dataset characteristics/suitability, version, quality findings, and justified preparation |
| `03_methodology.tex` | Agreed scenario, features, splits, models, validation/tuning, and metrics |
| `04_results.tex` | Measured comparisons and traceable tables/figures |
| `05_discussion.tex` | Interpretation, fair Kaggle comparison, attribution, and limitations |
| `06_conclusions_contributions.tex` | Supported conclusions and actual coding/writing/presentation contributions |

Keep the report consistent with [methodology.md](../docs/methodology.md), experiment evidence, and the [contribution record](../docs/contributions.md). Add inspected sources to `references.bib`, using citations such as `\cite{dataset}`; include exact external notebook/method versions and code attribution.

## Compile and review

With MiKTeX or TeX Live installed, open a terminal in `report/` and run:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Open `main.pdf` and review every page for readable text, sensible breaks, clear captions, and working links. Check the final `main.log` for errors, unresolved citations/references, and overfull boxes; earlier passes may request another run.

Check page count in the viewer or with `pdfinfo main.pdf`. The **completed report must be 5-8 pages**; the shorter draft is not padded to meet that length. Allocate space to justified methods and evidence, retain 11-point type and 1-inch margins, and shorten repetitive prose rather than compress formatting.

The root `.gitignore` excludes `main.pdf`, `build/`, and LaTeX temporary files. The original proposal and agreed final PDF remain eligible for Git.

## Using results and submitting

Use reviewed figures from `../results/figures/` (the graphics path in `main.tex`) and generated LaTeX tables from `../results/tables/`. Add `\includegraphics` or `\input` references only after the assets exist; explain each figure/table and link its experiment evidence.

After team review, store the agreed completed PDF at `report/final_report.pdf` and add its link to the root README. The report must link to Milestone 2, code, and the real final video. Verify sources, member contributions, access to links, length, and layout before submission. Compiling a draft checks its build and presentation, not scientific validity or reproducibility.
