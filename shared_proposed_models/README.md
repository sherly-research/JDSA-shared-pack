# Proposed Models Share Pack

This file is intended to understand the bifurcated-hybrid pipeline:
- Segmentation
- UNSUP branch (topic+embedding ranking)
- RB branch (POS/dependency noun-phrase extraction)
- Fusion-and-selection (HYBRID)

Start with: `docs/SHARE_PROTOCOL.md`.

## Notebook order
1. `00_build_fusion_input.ipynb`
2. `01_segmentation.ipynb`
3. `02_preprocess_unsup.ipynb`
4. `03_unsup_ate.ipynb`
5. `04_preprocess_rb.ipynb`
6. `05_rb_ate.ipynb`
7. `06_fusion_selection.ipynb`

## Data privacy
Inputs `dataset.csv` and `data_raw_no_duplikat.csv` were sanitized by removing the `user` column.


## Notebook map
See `docs/NOTEBOOK_MAP.md` for a quick guide to each notebook and its inputs/outputs.
