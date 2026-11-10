# Shared LaTeX report

The official report source is LaTeX here. Google Docs is not the official writing location. This is a drafting template, not a completed scientific report or final deliverable.

## What to edit

- `main.tex`: title, member names, shared formatting, section order, and project links.
- `sections/01_introduction.tex`: question, motivation, scope, and differentiation from relevant Kaggle work.
- `sections/02_data.tex`: source/version, quality audit, preparation, and limitations of synthetic data.
- `sections/03_methodology.tex`: prediction scenario, feature availability, splits, baselines/models, validation, tuning, and metrics.
- `sections/04_results.tex`: actual measured comparisons, tables, figures, and evidence links.
- `sections/05_discussion.tex`: interpretation, limitations, and fair comparison with external work.
- `sections/06_conclusions_contributions.tex`: supported conclusions and actual member contributions.
- `references.bib`: verified sources. Starter entries identify only the existing proposal, dataset source, and repository; add exact notebook/method references after inspecting them. Use citation keys such as `\cite{dataset}`.

Agree on an editor and reviewer for each section task; responsibilities are pending. Avoid simultaneous edits to the same file, keep formatting changes in `main.tex`, and cross-review the complete report so terminology and claims agree across sections.

## Compile and review

Use an existing local LaTeX installation (for example MiKTeX or TeX Live) with `pdflatex` and `bibtex`. No Python or ML environment is required to compile this template. Open a terminal in `report/` and run:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Open `main.pdf`. Read every page for clipped text, awkward breaks, readable tables, figure captions, and working links. Check `main.log` for errors, undefined citations/references, and overfull boxes. The first pass may request another run; assess the final pass after BibTeX and both subsequent LaTeX runs.

Check the page count in the PDF viewer or, if available, run `pdfinfo main.pdf`. The completed group report must be **5-8 pages**. A short placeholder template does not satisfy that requirement. A suggested writing budget is about 1 page for introduction, 1 for data, 1.5-2 for methodology, 1-1.5 for results, and 1-1.5 for discussion, conclusions, contributions, and references; adjust after real content exists. Confirm any course-specific page-count rules with the assignment instructions. Keep the standard 11-point font and 1-inch margins; reach the length through concise writing and appropriate content.

The root `.gitignore` excludes `main.pdf`, `build/`, and LaTeX temporary files. You may keep local preview files without committing them. No blanket PDF ignore rule is used: the original proposal and the agreed final PDF remain eligible for Git.

## Results and final submission

For a real figure, `main.tex` sets the graphics path to `../results/figures/`; use `\includegraphics` only when the named file exists. For a real generated LaTeX table, use `\input{../results/tables/ACTUAL_TABLE.tex}` after generating and reviewing it. These are instructions, not missing-asset references in the template. Link tables/figures to their experiment records.

Replace drafting placeholders only with agreed methods or verified findings. Document attribution for external methods and code. Keep the proposal and code links and replace the pending video text with the real final URL. Copy verified actual contributions from the shared record, checking that every member contributed to coding, writing, and presentation.

After team review of the completed report, store the agreed PDF at `report/final_report.pdf`. Do not rename the empty drafting template as a final report. At that point add a working final-PDF link to the root README. Check the final report's 5-8 page length, sources, proposal/code/video links, and visual layout again.

Successful compilation validates this template's build and layout only. It does not validate an experimental protocol, results, scientific conclusions, or project reproducibility.
