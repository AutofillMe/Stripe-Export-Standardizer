import os
from pathlib import Path

import pandas as pd
from numpy import diag_indices_from


def fileExists(path: str) -> bool:
    return Path(path).is_file()


def readConfig(path: str = r"./config.txt") -> list[str]:
    """
    Task:
    Reads in a file named `config.txt` as an ordered list of column keys.
    ---
    Notes:
    config.txt should be a list of column keys from the Stripe import as an
    ordered list separated by newlines.
    ---
    IN: path to config.txt (str) default: {pwd}/config.txt
    OUT: ordered list of column keys (list[str])
    """
    config = []

    if not fileExists(path):
        print(
            "Failed to read config.txt, please check that the file exists at the given path."
        )
        print(f"Path to config.txt: {path}")

    with open(path, "r") as f:
        config = [line.strip() for line in f if line.strip()]
    return config


def readStripeExport(path: str = r"./export.csv") -> pd.DataFrame:
    """
    Task:
    Reads in the unorganized Stripe export as a pandas DataFrame
    ---
    Notes:
    The Stripe export should be a .csv file
    ---
    IN: path to Stripe export (str) default: {pwd}/export.csv
    OUT: pandas DataFrame containing the Stripe export
    """
    if not fileExists(path):
        print(
            "Failed to read Stripe export, please check that the file exists at the given path."
        )
        print(f"Path to Stripe export: {path}")

    df = pd.read_csv(path)
    return df


def cleanStripeExport(df: pd.DataFrame) -> pd.DataFrame:
    """
    Task:
    Re-organizes the Stripe Export dataframe into a set order, based on the
    configuration from config.txt
    ---
    Notes:
    Will add columns in order of config.txt, and any columns not specified will be appended
    to the end unordered.
    ---
    IN: dataframe containing the unorganized stripe export (df.DataFrame)
    OUT: cleaned dataframe containing the stripe export (pd.DataFrame)
    """
    # TODO add me
    return df


def generateCSV(df: pd.DataFrame) -> None:
    df.to_csv("./out.csv")
    return None


def main() -> int | None:
    # TODO add logic
    # Read config
    #   - Create a list keys
    #   - return the list of keys
    # Read stripe export
    #   - create a df
    #   - return df
    # Standardize
    # Rebuild
    return 0


if __name__ == "__main__":
    main()
