from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd

def ensure_seg_key(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["comment_id"] = df["comment_id"].astype(str)
    df["seg_id"] = df["seg_id"].astype(str)
    if "seg_key" not in df.columns:
        df["seg_key"] = df["comment_id"] + "__" + df["seg_id"]
    return df

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--segments", default="data/segments_index.csv")
    ap.add_argument("--unsup", default="outputs/unsup_output.csv")
    ap.add_argument("--rb", default="outputs/rb_output.csv")
    ap.add_argument("--out", default="data/dataset_merged_with_unsup_rb_aspects_ALLCOLS.csv")
    args = ap.parse_args()

    segments = ensure_seg_key(pd.read_csv(args.segments))
    unsup = ensure_seg_key(pd.read_csv(args.unsup))
    rb = ensure_seg_key(pd.read_csv(args.rb))

    unsup_keep = [c for c in ["seg_key","aspect_terms_unsup","top_aspect_terms_unsup","top_aspect_cos_unsup",
                             "terms_ranked","cos_ranked","fallback_mode","cluster_unsup"] if c in unsup.columns]
    rb_keep = [c for c in ["seg_key","aspect_terms_rb_clean","aspect_terms_rb","aspect_terms_rb_raw",
                          "rb_lang_used","seg_text_processed","seg_text_clean","interj_removed"] if c in rb.columns]

    merged = segments.merge(rb[rb_keep], on="seg_key", how="left").merge(unsup[unsup_keep], on="seg_key", how="left")
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    merged.to_csv(args.out, index=False)
    print("Wrote:", args.out, "rows:", len(merged), "unique seg_key:", merged["seg_key"].nunique())

if __name__ == "__main__":
    main()
