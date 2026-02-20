# Bifurcated-hybrid ATE pipeline 

This pack organizes the **proposed model notebooks** (UNSUP, RB, HYBRID) and their **derived inputs/outputs**.

## What is included
- `notebooks/`: cleaned notebooks in execution order.
- `data/`: derived inputs needed to reproduce the fusion stage.
- `outputs/`: derived outputs from UNSUP / RB / HYBRID (with unique `seg_key`).
- `data/samples/`: small samples (200 rows) for quick inspection.
- `raw_inputs/`: original files as provided (for traceability).

## Key alignment protocol
- `seg_id` is local (can repeat across comments). Use **unique segment key**:
  - `seg_key = comment_id__seg_id`
- All merges in the fusion stage must use `seg_key` (or `comment_id` + `seg_id`).

## Fusion input (missing file in original directory)
The original fusion notebook expects:
- `data/dataset_merged_with_unsup_rb_aspects_ALLCOLS.csv`

This pack provides it, built by merging:
- `outputs/unsup_output.csv`
- `outputs/rb_output.csv`

See `notebooks/00_build_fusion_input.ipynb`.

## Removing the `user` attribute
Columns named `user` were removed from shared inputs (`dataset.csv`, `data_raw_no_duplikat.csv`) to reduce sensitive identifiers.

## How you can run (lightweight)
1) Inspect samples:
- `data/samples/sample_fusion_input_200.csv`
- `data/samples/sample_unsup_200.csv`, `sample_rb_200.csv`, `sample_hybrid_200.csv`

2) Rebuild fusion input (optional):
```bash
python -m pip install pandas
python scripts/run_fusion_minimal.py --fusion_input data/dataset_merged_with_unsup_rb_aspects_ALLCOLS.csv --out outputs/hybrid_from_merge_minimal.csv
```

Note: `scripts/run_fusion_minimal.py` is a minimal, transparent baseline to show the merge mechanics.
The full HYBRID logic remains in `notebooks/06_fusion_selection.ipynb`.


## Master segment universe
This pack uses `data/segments_index.csv` as the master segment universe (segment-level unit in the manuscript).
