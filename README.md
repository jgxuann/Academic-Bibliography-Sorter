# Academic-Bibliography-Sorter
Python script and finalized bibliography file sorted according to academic standards (e.g., author surname alphabetically).

# Academic Bibliography Sorter

This repository contains a utility Python script and the final, corrected bibliography file for our research project. The main purpose is to automate the sorting of LaTeX `\bibitem` entries alphabetically by the first author's surname, addressing common reviewer requests for proper citation ordering.

---

## 🚀 Repository Contents

| File Name | Description |
| :--- | :--- |
| `bib.txt` | **Original Source File.** The raw, unsorted, and uncorrected list of `\bibitem` entries (kept for archival/verification purposes). |
| `main.py` | The custom Python script used to read the raw data, extract author names, sort the entries, and output the final file. |
| `bib_sorted.txt` | **Final Deliverable.** This file contains the complete bibliography list, professionally sorted alphabetically by author surname, and includes necessary character encoding fixes. |

---

## ✨ Why This Repository Exists

This project addresses the critical reviewer feedback:

> **Reviewer Comment:** The list should be sorted alphabetically.

The `bib_sorted.txt` file ensures strict adherence to:

1.  **Alphabetical Order:** All `\bibitem` entries are sorted based on the **first author's surname** (A-Z).
2.  **Character Encoding:** All special character issues (e.g., en-dashes, umlauts, non-standard hyphens) have been corrected to ensure successful LaTeX compilation.

---

## 🛠️ Usage Guide

### 1. Using the Script (Optional)

If you wish to re-run the sorting process, follow these steps:

1.  Ensure Python is installed on your system.
2.  Place your raw bibliography content into the `bib.txt` file.
3.  Execute the script from your terminal:
    ```bash
    python3 main.py
    ```
4.  The script will report the number of references detected and save the sorted output to `sorted_bib.txt` (or the file name specified in the script).

### 2. Implementing the Sorted File

To integrate the sorted bibliography into your main LaTeX document:

* Copy the content of **`bibliography_sorted.tex`** and paste it directly into your main `.tex` file, replacing the old `\begin{thebibliography}{00}` and `\end{thebibliography}` block.

### Future Recommendation

For future projects, it is highly recommended to transition to a **BibTeX** (`.bib`) file format with a citation management tool. This allows the LaTeX compiler to handle all sorting and formatting automatically based on your chosen style (e.g., `\bibliographystyle{plain}`).

---
