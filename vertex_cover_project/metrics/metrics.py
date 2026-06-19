import networkx as nx

def connectivity(edges, num_devices):

    total_possible = (
        num_devices *
        (num_devices - 1)
    ) / 2

    return (
        len(edges) /
        total_possible
    ) * 100

def graph_density(graph):

    return nx.density(graph)

def average_degree(graph):

    return (
        sum(
            dict(graph.degree()).values()
        )
        /
        graph.number_of_nodes()
    )

def energy_saving(
    cover,
    active_nodes
):

    if len(active_nodes) == 0:
        return 0

    return (
        1 -
        len(cover) /
        len(active_nodes)
    ) * 100

def error_percentage(
    current_cover,
    optimal_cover
):

    if len(optimal_cover) == 0:
        return 0

    return (
        (
            len(current_cover)
            -
            len(optimal_cover)
        )
        /
        len(optimal_cover)
    ) * 100

def approximation_ratio(
    current_cover,
    optimal_cover
):

    if len(optimal_cover) == 0:
        return 1

    return (
        len(current_cover)
        /
        len(optimal_cover)
    )

def connected_components(graph):
    return nx.number_connected_components(graph)