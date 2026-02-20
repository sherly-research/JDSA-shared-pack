# Notebook Map 
This file explains what each shared notebook does, and the expected inputs/outputs.
## Execution order
1. `00_build_fusion_input.ipynb` — Build fusion input by left-joining RB/UNSUP outputs onto the master segment universe (segments_index).
2. `01_segmentation.ipynb` — Segment raw comments into sentence-like segments; produce seg_id and segment texts.
3. `02_preprocess_unsup.ipynb` — Normalize/clean segments for the UNSUP branch (e.g., lowercasing, spacing, noise tokens).
4. `03_unsup_ate.ipynb` — UNSUP candidate discovery + semantic-context ranking; outputs per-segment candidate lists.
5. `04_preprocess_rb.ipynb` — Normalize/clean segments for the RB branch, including language fallback if used.
6. `05_rb_ate.ipynb` — RB extraction of noun phrases / candidates using POS + dependency patterns.
7. `06_fusion_selection.ipynb` — Hybrid fusion-and-selection (PMI gate + context-fit ranking + overlap bonus + fallbacks).
8. `99_quick_review.ipynb` — Fast walkthrough using 200-row samples: show seg_key, branch outputs, and illustrative overlap/empty cases.

## Inputs and outputs
### `00_build_fusion_input.ipynb`
Build fusion input by left-joining RB/UNSUP outputs onto the master segment universe (segments_index).

**Inputs**
- `data/segments_index.csv`
- `outputs/rb_output.csv`
- `outputs/unsup_output.csv`

**Outputs**
- `data/dataset_merged_with_unsup_rb_aspects_ALLCOLS.csv`

---
### `01_segmentation.ipynb`
Segment raw comments into sentence-like segments; produce seg_id and segment texts.

**Inputs**
- `raw_inputs/data/dataset.csv (sanitized)`
- `raw_inputs/data/data_raw_no_duplikat.csv (sanitized)`

**Outputs**
- `data/segments_index.csv (or equivalent segment table)`

---
### `02_preprocess_unsup.ipynb`
Normalize/clean segments for the UNSUP branch (e.g., lowercasing, spacing, noise tokens).

**Inputs**
- `data/segments_index.csv`

**Outputs**
- `intermediate processed text columns used by UNSUP ranking`

---
### `03_unsup_ate.ipynb`
UNSUP candidate discovery + semantic-context ranking; outputs per-segment candidate lists.

**Inputs**
- `data/segments_index.csv`
- `preprocessed UNSUP text`

**Outputs**
- `outputs/unsup_output.csv`

---
### `04_preprocess_rb.ipynb`
Normalize/clean segments for the RB branch, including language fallback if used.

**Inputs**
- `data/segments_index.csv`

**Outputs**
- `intermediate processed text columns used by RB extraction`

---
### `05_rb_ate.ipynb`
RB extraction of noun phrases / candidates using POS + dependency patterns.

**Inputs**
- `data/segments_index.csv`
- `preprocessed RB text`

**Outputs**
- `outputs/rb_output.csv`

---
### `06_fusion_selection.ipynb`
Hybrid fusion-and-selection (PMI gate + context-fit ranking + overlap bonus + fallbacks).

**Inputs**
- `data/dataset_merged_with_unsup_rb_aspects_ALLCOLS.csv`

**Outputs**
- `outputs/hybrid_output.csv (best term + top-k terms)`

---
### `99_quick_review.ipynb`
Fast walkthrough using 200-row samples: show seg_key, branch outputs, and illustrative overlap/empty cases.

**Inputs**
- `data/samples/*.csv`

**Outputs**
- `(none)`

---

## Key alignment
Use `seg_key = comment_id__seg_id` as the unique segment identifier for merges and evaluations.

## Privacy
Shared inputs have the `user` column removed.
