import csv

def create_detailed_csv(file_name):

    with open(
        file_name,
        "w",
        newline="",
        encoding="utf-8"
    ) as f:

        writer = csv.writer(f)

        writer.writerow([
            "Devices",
            "Run",
            "Algorithm",
            "VCSize",
            "ExecutionTime",
            "Density",
            "Error",
            "ApproximationRatio",
            "GraphFile"
        ])

def write_detailed(
    file_name,
    row
):
    with open(
        file_name,
        "a",
        newline="",
        encoding="utf-8"
    ) as f:

        writer = csv.writer(f)

        writer.writerow(row)

def create_summary_csv(file_name):

    with open(
        file_name,
        "w",
        newline="",
        encoding="utf-8"
    ) as f:

        writer = csv.writer(f)

        writer.writerow([
            "Devices",
            "Algorithm",
            "AvgVCSize",
            "AvgExecutionTimeMs",
            "StdExecutionTimeMs",
            "AvgDensity",
            "AvgConnectivity",
            "AvgEnergySaving",
            "AvgError",
            "AvgApproximationRatio",
            "BestVCSize",
            "BestExecutionTimeMs"
        ])

def write_summary(
    file_name,
    row
):
    """
    Adiciona uma linha ao CSV de resumo.

    Parâmetros:
        file_name (str): caminho do CSV
        row (list): dados da linha
    """

    with open(
        file_name,
        "a",
        newline="",
        encoding="utf-8"
    ) as f:

        writer = csv.writer(f)

        writer.writerow(row)