# Funções matemáticas
import math
# Geração de números aleatórios
import random
# Biblioteca para criação e análise de grafos
import networkx as nx

def distance(p1, p2):
    return math.sqrt(
        (p1[0]-p2[0])**2 +
        (p1[1]-p2[1])**2
    )

def generate_graph(
    num_devices,
    area_size,
    wifi_range,
    top_percent,
    band_height_percent
):

    band_height = area_size * band_height_percent

    while True:

        positions = {}

        for i in range(num_devices):

            x = random.uniform(0, area_size)

            if random.random() < top_percent:

                y = random.uniform(
                    area_size-band_height,
                    area_size
                )

            else:

                y = random.uniform(
                    0,
                    band_height
                )

            positions[i] = (x, y)

        edges = []

        for i in range(num_devices):
            for j in range(i+1, num_devices):

                if distance(
                    positions[i],
                    positions[j]
                ) <= wifi_range:

                    edges.append((i, j))

        G = nx.Graph()
        G.add_nodes_from(range(num_devices))
        G.add_edges_from(edges)

        if nx.number_connected_components(G) == 1:

            return {
                "graph": G,
                "positions": positions,
                "edges": edges
            }