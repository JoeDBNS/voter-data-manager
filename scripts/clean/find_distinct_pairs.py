"""
find_distinct_pairs.py
----------------------
Scans the Michigan voter file for distinct code/name pairs across one or more
column sets in a single pass.

Usage
-----
# Run all configured column sets:
    python scripts/clean/find_distinct_pairs.py

# Run a specific column set by key:
    python scripts/clean/find_distinct_pairs.py house_districts

# Run multiple specific column sets:
    python scripts/clean/find_distinct_pairs.py house_districts senate_districts

Configuration
-------------
Add entries to COLUMN_SETS below to scan additional fields without touching
the rest of the script.  Each entry is:

    "key": {
        "code_col":  "<CSV column name for the code>",
        "name_col":  "<CSV column name for the name>",
        "out_file":  "<output CSV filename, relative to this script's directory>",
    }
"""

import csv
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration — edit here to add / remove column sets
# ---------------------------------------------------------------------------
COLUMN_SETS = {
    "house_districts": {
        "code_col": "STATE_HOUSE_DISTRICT_CODE",
        "name_col": "STATE_HOUSE_DISTRICT_NAME",
        "out_file": "house_districts.csv",
    },
    "senate_districts": {
        "code_col": "STATE_SENATE_DISTRICT_CODE",
        "name_col": "STATE_SENATE_DISTRICT_NAME",
        "out_file": "senate_districts.csv",
    },
    "congress_districts": {
        "code_col": "US_CONGRESS_DISTRICT_CODE",
        "name_col": "US_CONGRESS_DISTRICT_NAME",
        "out_file": "congress_districts.csv",
    },
    "county_commissioner_districts": {
        "code_col": "COUNTY_COMMISSIONER_DISTRICT_CODE",
        "name_col": "COUNTY_COMMISSIONER_DISTRICT_NAME",
        "out_file": "county_commissioner_districts.csv",
    },
    "uocava_statuses": {
        "code_col": "UOCAVA_STATUS_CODE",
        "name_col": "UOCAVA_STATUS_NAME",
        "out_file": "uocava_statuses.csv",
    },
}

INPUT_FILE = "mi_voter_list-march.csv"
SCRIPT_DIR = Path(__file__).parent.parent / "reference_data"

# ---------------------------------------------------------------------------
# Resolve which column sets to run
# ---------------------------------------------------------------------------
requested_keys = sys.argv[1:]

if requested_keys:
    unknown = [k for k in requested_keys if k not in COLUMN_SETS]
    if unknown:
        print(f"ERROR: unknown column set(s): {', '.join(unknown)}", file=sys.stderr)
        print(f"Available: {', '.join(COLUMN_SETS)}", file=sys.stderr)
        sys.exit(1)
    active_sets = {k: COLUMN_SETS[k] for k in requested_keys}
else:
    active_sets = COLUMN_SETS

# ---------------------------------------------------------------------------
# Load previously saved pairs for each active set
# ---------------------------------------------------------------------------
state = {}  # key -> {"pairs": set, "code_col": str, "name_col": str, "out_file": Path, "new": int}

for key, cfg in active_sets.items():
    out_path = SCRIPT_DIR / cfg["out_file"]
    pairs = set()

    if out_path.exists():
        with open(out_path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # skip header
            for row in reader:
                if row:
                    pairs.add((row[0].strip(), row[1].strip()))
        print(f"[{key}] Loaded {len(pairs)} existing pairs from {cfg['out_file']}", file=sys.stderr)

    state[key] = {
        "pairs":    pairs,
        "code_col": cfg["code_col"],
        "name_col": cfg["name_col"],
        "out_path": out_path,
        "new":      0,
    }

# ---------------------------------------------------------------------------
# Single-pass scan
# ---------------------------------------------------------------------------
row_count = 0

with open(INPUT_FILE, newline="", encoding="latin-1") as f:
    reader = csv.reader(f)
    headers = next(reader)

    # Resolve column indices once before the loop
    for s in state.values():
        s["code_idx"] = headers.index(s["code_col"])
        s["name_idx"] = headers.index(s["name_col"])

    # Open all output files for appending upfront to avoid repeated open/close
    out_handles = {}
    out_writers = {}
    for key, s in state.items():
        fh = open(s["out_path"], "a", newline="", encoding="utf-8")
        out_handles[key] = fh
        out_writers[key] = csv.writer(fh)
        # Write header if the file is new / empty
        if s["out_path"].stat().st_size == 0 if s["out_path"].exists() else True:
            out_writers[key].writerow([s["code_col"], s["name_col"]])

    try:
        for row in reader:
            for key, s in state.items():
                pair = (row[s["code_idx"]].strip(), row[s["name_idx"]].strip())
                if pair not in s["pairs"]:
                    s["pairs"].add(pair)
                    s["new"] += 1
                    out_writers[key].writerow(pair)

            row_count += 1
            if row_count % 500_000 == 0:
                # Flush all handles so partial results are safely on disk
                for fh in out_handles.values():
                    fh.flush()
                print(f"  ...{row_count:,} rows processed", file=sys.stderr)
    finally:
        for fh in out_handles.values():
            fh.close()

# ---------------------------------------------------------------------------
# Print results
# ---------------------------------------------------------------------------
for key, s in state.items():
    print(f"\n{'=' * 50}")
    print(f"  {key}  ({s['out_path'].name})")
    print(f"{'=' * 50}")
    print(f"  {'CODE':<10} {'NAME'}")
    print(f"  {'-' * 38}")
    for code, name in sorted(s["pairs"]):
        print(f"  {code:<10} {name}")
    print(f"\n  Total unique pairs : {len(s['pairs'])}")
    print(f"  New this run       : {s['new']}")
    print(f"  Saved to           : {s['out_path']}")

print(f"\nTotal rows processed: {row_count:,}")
