"""
##########################################################################################
Title: Consensus Scoring and Filtering of GOLD Docking Results

Author: Dr. Mine Isaoglu  
Principal Investigator: Prof. Dr. Serdar Durdagi  
Affiliation: Computational Drug Design Center (HITMER),  
             Faculty of Pharmacy, Bahçeşehir University, Istanbul, Turkey  
Version: December 2024 
##########################################################################################
"""

import sys
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def normalize(series: pd.Series) -> pd.Series:
    """Return min–max normalised *series* spanning the closed interval [0, 1]."""
    return (series - series.min()) / (series.max() - series.min())


def main(input_csv: str, threshold: float = 0.5) -> None:
    """Execute the consensus‑scoring workflow on *input_csv*.

    Parameters
    ----------
    input_csv : str
        Path to the docking results CSV file.
    threshold : float, optional
        Minimum consensus score required to retain a molecule (default = 0.5).
    """
    # Resolve and validate the input path
    csv_path = Path(input_csv).expanduser().resolve()
    if not csv_path.is_file():
        sys.exit(f"Error: Cannot find input file '{csv_path}'.")

    # Read the docking results
    df = pd.read_csv(csv_path)

    # Select only rows with positive fitness values in both metrics
    filtered_df = df[(df["PLP.Fitness"] > 0) & (df["Goldscore.Fitness"] > 0)].copy()

    # Normalisation
    filtered_df["PLP.Fitness.Norm"] = normalize(filtered_df["PLP.Fitness"])
    filtered_df["Goldscore.Fitness.Norm"] = normalize(filtered_df["Goldscore.Fitness"])

    # Consensus score (weighted arithmetic mean)
    filtered_df["Consensus.Score"] = (
        filtered_df["PLP.Fitness.Norm"] * 0.6
        + filtered_df["Goldscore.Fitness.Norm"] * 0.4
    )

    # Retain only high‑scoring ligands
    high_consensus = filtered_df[filtered_df["Consensus.Score"] >= threshold]

    # Write results
    output_path = csv_path.with_name("high_consensus_molecules.csv")
    high_consensus.to_csv(output_path, index=False)
    print(
        f"Filtered dataset saved as '{output_path.name}' ")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: python consensus_scoring.py <input_csv>")

    main(sys.argv[1])
