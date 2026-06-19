import os

TOP_PERCENT = 0.7
BAND_HEIGHT_PERCENT = 0.20

GRAPH_FOLDER = "output/graphs"
PLOTS_FOLDER = "output/plots"

os.makedirs(GRAPH_FOLDER, exist_ok=True)
os.makedirs(PLOTS_FOLDER, exist_ok=True)

DETAILED_CSV = "output/vertex_cover_detailed.csv"
SUMMARY_CSV = "output/vertex_cover_summary.csv"