"""
corpus.py

This module provides utilities for working with corpora
(i.e. collections of found phrases bounded by time).
It defines the required schema for every
corpus and a function `load_corpus` to properly load data.

Supported file formats:
- CSV (.csv): comma separated values
- TSV (.tsv): tab separated values
- JSON (.json): an array of objects, one per phrase
"""

from pathlib import Path
import pandas as pd


# Columns required in every corpus file:
# - phrase_idx: auto-incremented index of each phrase (integer or string).
# - phrase: phrase text copied from a found source (string).
# - phrase_recorded_date: date the phrase was logged (string, YYYY-MM-DD).
# - phrase_reference_link: source URL (string, may be empty).
REQUIRED_COLUMNS = [
    "phrase_idx",
    "phrase",
    "phrase_recorded_date",
    "phrase_reference_link",
]


def load_corpus(path: str | Path, file_format: str = "auto"):
    """
    Load a corpus file into a pandas DataFrame and validate required columns.

    Steps:
      1. Determine the file format (either from the extension or the
         explicit `file_format` argument).
      2. Use pandas to read the file into a DataFrame.
      3. Check that all required columns are present.
      4. Return the DataFrame for further analysis.

    Supported formats:
      - csv  : comma separated values
      - tsv  : tab separated values
      - json : JSON array of objects, one per phrase

    Args:
        path: Path to the corpus file.
        file_format: 'auto' (infer from extension) or explicitly
            'csv', 'tsv', or 'json'.

    Returns:
        pandas.DataFrame containing all rows in the corpus file.

    Raises:
        ValueError: If the format is unsupported or required columns
            are missing.
    """
    path = Path(path)
    choice = file_format.lower()

    # Infer type if 'auto'
    if choice == "auto":
        suffix = path.suffix.lower()
        if suffix == ".csv":
            choice = "csv"
        elif suffix == ".tsv":
            choice = "tsv"
        elif suffix == ".json":
            choice = "json"
        else:
            raise ValueError(
                f"Cannot infer file type '{suffix}'. Use --format csv, "
                "tsv, or json."
            )

    # Load according to chosen format
    if choice == "csv":
        df = pd.read_csv(path)
    elif choice == "tsv":
        df = pd.read_csv(path, sep="\t")
    elif choice == "json":
        df = pd.read_json(path)
    else:
        raise ValueError("file_format must be auto, csv, tsv, or json")

    # Validate required columns
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    return df
