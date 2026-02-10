"""
Portfolio Data Extraction (Sanitized Example)

This script demonstrates a typical workflow:
1) Read DB connection string from environment (placeholder)
2) Build a parameterised query pattern (placeholder)
3) Load results into pandas
4) Select/rename columns
5) Export cleaned CSV

NOTE:
- This is a sanitized example. No real credentials, table names, or internal paths are included.
"""

from __future__ import annotations

import argparse
import os
import sys
from typing import List

import pandas as pd


def build_query(nodes: List[str]) -> str:
    """
    Build a query string (placeholder example).

    In real work, prefer parameterised queries to avoid SQL injection.
    Here we only show the pattern.
    """
    nodes_string = ", ".join([f"'{n}'" for n in nodes])
    query = f"""
    SELECT parent_portfolio AS PARENT,
           child_portfolio  AS PORTFOLIO
    FROM portfolio_hierarchy
    WHERE hierarchy_tree_id IN ({nodes_string})
    """
    return query.strip()


def fetch_data(query: str) -> pd.DataFrame:
    """
    Placeholder for DB fetch logic.

    In a real script, this is where you'd use pyodbc/sqlalchemy and pd.read_sql_query().
    For public sharing, we return dummy data to demonstrate downstream transformations.
    """
    # Dummy dataset (safe)
    return pd.DataFrame(
        {
            "PARENT": ["CCORP", "HCORP"],
            "PORTFOLIO": ["PORT_A", "PORT_B"],
        }
    )


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Select and return cleaned output columns."""
    out = df[["PARENT", "PORTFOLIO"]].copy()
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Sanitized portfolio data extraction example.")
    parser.add_argument(
        "--nodes",
        nargs="+",
        default=["CCORP", "HCORP"],
        help="Example hierarchy nodes (dummy values).",
    )
    parser.add_argument(
        "--out",
        default="src/sample_data/sample_output.csv",
        help="Output CSV path.",
    )
    args = parser.parse_args()

    # Example: connection string from environment (placeholder)
    _connection_string = os.getenv("DB_CONNECTION_STRING", "NOT_SET")

    query = build_query(args.nodes)
    df = fetch_data(query)
    cleaned = clean_data(df)

    # Make sure folder exists
    os.makedirs(os.path.dirname(args.out), exist_ok=True)

    cleaned.to_csv(args.out, index=False)
    print(f"Saved cleaned output to: {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
