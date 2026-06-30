"""
Autor: Carlos Erlan Olival Lima

Framework Experimental para Comparação de Algoritmos
Vertex Cover em Redes Mesh

Algoritmos:

1. Brute Force
2. Backtracking
3. Greedy Vertex Cover
4. Edge-Greedy Heuristic
"""

import os
import time
import statistics

from graph_generation.graph_generator import generate_graph

from algorithms import brute_force
from algorithms import backtracking
from algorithms import greedy
from algorithms import edge_greedy

from metrics.metrics import (
    connectivity,
    graph_density,
    average_degree,
    energy_saving,
    error_percentage,
    approximation_ratio
)

from visualizations.graph_visualizer import save_graph

from reports.csv_writer import (
    create_detailed_csv,
    create_summary_csv,
    write_detailed,
    write_summary
)

from reports.plot_generator import (
    plot_execution_time_comparison,
    plot_vc_size_comparison,
    plot_error_comparison,
    plot_approximation_comparison,
    plot_energy_comparison
)

def benchmark_algorithm(func, args, benchmark_runs):
    """
    Executa um algoritmo várias vezes sobre o mesmo grafo
    para obter um tempo médio de execução.
    """

    result = None

    start = time.perf_counter()

    for _ in range(benchmark_runs):
        result = func(*args)

    elapsed = (
        time.perf_counter() - start
    ) * 1000

    avg_time = elapsed / benchmark_runs

    return result, avg_time
# ==========================================================
# ENTRADA DO USUÁRIO
# ==========================================================

MIN_DEVICES = int(
    input("Número mínimo de dispositivos: ")
)

MAX_DEVICES = int(
    input("Número máximo de dispositivos: ")
)

NUM_RUNS = int(
    input("Número de repetições por cenário: ")
)

AREA_SIZE = float(
    input("Tamanho da área: ")
)

WIFI_RANGE = float(
    input("Alcance WiFi: ")
)

# ==========================================================
# CONFIGURAÇÕES
# ==========================================================

TOP_PERCENT = 0.7
BAND_HEIGHT_PERCENT = 0.20

GRAPH_FOLDER = "graphs"
PLOTS_FOLDER = "plots"

DETAILED_CSV = "vertex_cover_detailed.csv"
SUMMARY_CSV = "vertex_cover_summary.csv"

os.makedirs(
    GRAPH_FOLDER,
    exist_ok=True
)

os.makedirs(
    PLOTS_FOLDER,
    exist_ok=True
)

# ==========================================================
# CRIA CSVs
# ==========================================================

create_detailed_csv(
    DETAILED_CSV
)

create_summary_csv(
    SUMMARY_CSV
)

# ==========================================================
# ESTRUTURAS PARA GRÁFICOS FINAIS
# ==========================================================

device_axis = []

avg_time_bf = []
avg_time_bt = []
avg_time_greedy = []
avg_time_edge = []

avg_vc_bf = []
avg_vc_bt = []
avg_vc_greedy = []
avg_vc_edge = []

avg_error_greedy = []
avg_error_edge = []

avg_ratio_greedy = []
avg_ratio_edge = []

avg_energy_bf = []
avg_energy_bt = []
avg_energy_greedy = []
avg_energy_edge = []

# ==========================================================
# LOOP PRINCIPAL
# ==========================================================

for devices in range(
    MIN_DEVICES,
    MAX_DEVICES + 1
):

    print(
        f"\nExecutando cenário com "
        f"{devices} dispositivos..."
    )

    device_axis.append(devices)

    algorithms_stats = {

        "BruteForce": [],
        "Backtracking": [],
        "Greedy": [],
        "EdgeGreedy": []
    }

    for run in range(
        1,
        NUM_RUNS + 1
    ):

        # ==================================================
        # GERA GRAFO
        # ==================================================

        graph_data = generate_graph(
            devices,
            AREA_SIZE,
            WIFI_RANGE,
            TOP_PERCENT,
            BAND_HEIGHT_PERCENT
        )

        graph = graph_data["graph"]
        positions = graph_data["positions"]
        edges = graph_data["edges"]

        # ==================================================
        # BRUTE FORCE
        # ==================================================

        bf_result, bf_time = benchmark_algorithm(
            brute_force.solve,
            (edges, devices),
            1
        )

        optimal_cover = bf_result["cover"]

        # ==================================================
        # BACKTRACKING
        # ==================================================

        bt_result, bt_time = benchmark_algorithm(
            backtracking.solve,
            (edges, devices),
            200
        )

        # ==================================================
        # GREEDY
        # ==================================================

        greedy_result, greedy_time = benchmark_algorithm(
            greedy.solve,
            (edges,),
            1000
        )

        # ==================================================
        # EDGE GREEDY
        # ==================================================

        edge_result, edge_time = benchmark_algorithm(
            edge_greedy.solve,
            (edges,),
            1000
        )

        # ==================================================
        # MÉTRICAS DO GRAFO
        # ==================================================

        density = graph_density(graph)

        avg_degree = average_degree(graph)

        conn = connectivity(
            edges,
            devices
        )

        # ==================================================
        # PROCESSA CADA ALGORITMO
        # ==================================================

        results = {

            "BruteForce":
                (bf_result, bf_time),

            "Backtracking":
                (bt_result, bt_time),

            "Greedy":
                (greedy_result, greedy_time),

            "EdgeGreedy":
                (edge_result, edge_time)
        }

        for alg_name, (
            result,
            exec_time
        ) in results.items():

            cover = result["cover"]

            active_nodes = set()

            for u, v in edges:

                active_nodes.add(u)
                active_nodes.add(v)

            energy = energy_saving(
                cover,
                active_nodes
            )

            error = error_percentage(
                cover,
                optimal_cover
            )

            ratio = approximation_ratio(
                cover,
                optimal_cover
            )

            # ==============================================
            # SALVA IMAGEM
            # ==============================================

            graph_file = (
                f"{GRAPH_FOLDER}/"
                f"N{devices}_"
                f"run{run}_"
                f"{alg_name}.png"
            )

            save_graph(
                graph,
                positions,
                cover,
                graph_file,
                alg_name
            )

            # ==============================================
            # SALVA CSV DETALHADO
            # ==============================================

            write_detailed(
                DETAILED_CSV,
                [
                    devices,
                    run,
                    alg_name,
                    len(cover),
                    round(exec_time, 4),
                    round(density, 4),
                    round(error, 4),
                    round(ratio, 4),
                    graph_file
                ]
            )

            algorithms_stats[
                alg_name
            ].append(
                {
                    "vc": len(cover),
                    "time": exec_time,
                    "error": error,
                    "ratio": ratio,
                    "energy": energy
                }
            )

            graph_metrics = {
                "density": [],
                "connectivity": [],
                "average_degree": []
            }

    # ======================================================
    # RESUMO POR QUANTIDADE DE DISPOSITIVOS
    # ======================================================

    for alg_name in algorithms_stats:

        stats = algorithms_stats[
            alg_name
        ]

        avg_vc = statistics.mean(
            [x["vc"] for x in stats]
        )

        avg_time = statistics.mean(
            [x["time"] for x in stats]
        )

        std_time = statistics.stdev(
            [x["time"] for x in stats]
        ) if len(stats) > 1 else 0

        avg_error = statistics.mean(
            [x["error"] for x in stats]
        )

        avg_ratio = statistics.mean(
            [x["ratio"] for x in stats]
        )

        avg_energy = statistics.mean(
            [x["energy"] for x in stats]
        )

        best_vc = min(
            [x["vc"] for x in stats]
        )

        best_time = min(
            [x["time"] for x in stats]
        )

        write_summary(
            SUMMARY_CSV,
            [
                devices,
                alg_name,
                round(avg_vc, 4),
                round(avg_time, 4),
                round(std_time, 4),
                round(density, 4),
                round(conn, 4),
                round(avg_energy, 4),
                round(avg_error, 4),
                round(avg_ratio, 4),
                best_vc,
                round(best_time, 4)
            ]
        )

        # armazenamento para gráficos

        if alg_name == "BruteForce":
            avg_time_bf.append(avg_time)
            avg_vc_bf.append(avg_vc)
            avg_energy_bf.append(avg_energy)

        elif alg_name == "Backtracking":
            avg_time_bt.append(avg_time)
            avg_vc_bt.append(avg_vc)
            avg_energy_bt.append(avg_energy)

        elif alg_name == "Greedy":
            avg_time_greedy.append(avg_time)
            avg_vc_greedy.append(avg_vc)
            avg_error_greedy.append(avg_error)
            avg_ratio_greedy.append(avg_ratio)
            avg_energy_greedy.append(avg_energy)

        elif alg_name == "EdgeGreedy":
            avg_time_edge.append(avg_time)
            avg_vc_edge.append(avg_vc)
            avg_error_edge.append(avg_error)
            avg_ratio_edge.append(avg_ratio)
            avg_energy_edge.append(avg_energy)

# ==========================================================
# GRÁFICOS FINAIS
# ==========================================================

plot_execution_time_comparison(
    device_axis,
    avg_time_bf,
    avg_time_bt,
    avg_time_greedy,
    avg_time_edge,
    f"{PLOTS_FOLDER}/execution_time_comparison.png"
)

print("\nExperimento finalizado.")
print("CSV detalhado gerado.")
print("CSV resumo gerado.")
print("Imagens dos grafos geradas.")
print("Gráficos finais gerados.")