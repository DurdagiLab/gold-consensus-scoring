# Consensus Scoring Tool for GOLD Docking

This script implements a consensus scoring strategy to prioritize ligands based on docking results obtained from the **GOLD molecular docking software**. It combines two scoring functions - **PLP.Fitness** and **Goldscore.Fitness** - to generate a weighted consensus score and filters molecules exceeding a defined threshold.

# Description
The scoring protocol is based on retrospective analysis and incorporates the following steps:

1. **Input parsing** - Reads the user-supplied GOLD CSV output.  
2. **Data cleaning** - Retains only ligands with positive scores in both PLP and Goldscore fields.  
3. **Min-max normalisation** - Scales each scoring function independently to the [0, 1] range.  
4. **Consensus scoring** - Computes an aggregated score using the formula:  
   **Consensus = 0.60 × PLP + 0.40 × Goldscore**  
5. **Filtering** - Extracts ligands with consensus scores ≥ 0.50 by default.

The final results are saved to `high_consensus_molecules.csv`.

# Requirements & Installation

Required Python version
- `Python ≥ 3.8`

Dependencies:
- `pandas`  
- `matplotlib` *(optional – for visualization only)*

You can install the required libraries using pip:

> pip install pandas matplotlib

# Input Format
The input file must be a comma-separated values (CSV) file exported from GOLD docking software. It should contain at least the following case-sensitive column headers:

1. PLP.Fitness
2. Goldscore.Fitness

**Rows with non-positive values in either of these columns are excluded prior to normalization to ensure statistical robustness.

# Usage
To run the script, execute the following command from the terminal, providing the path to the docking results CSV file as an argument:

> python gold-consensus-scoring.py docking_results.csv

**By default, the script filters ligands with a consensus score ≥ 0.50 based on normalized PLP and Goldscore fitness values. You may adjust the threshold or weights by editing the script if necessary.

# Citation
If you use this tool in your research or publication, please cite it as follows:

Isaoğlu, M., & Durdağı, S. (2025). Consensus Scoring Tool for GOLD Docking (Version 1.0) [Computer software]. https://github.com/DurdagiLab/gold-consensus-scoring
