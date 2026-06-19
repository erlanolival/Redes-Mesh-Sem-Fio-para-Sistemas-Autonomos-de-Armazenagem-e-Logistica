import matplotlib.pyplot as plt
import networkx as nx

def save_graph(
    graph,
    positions,
    cover,
    file_name,
    title
):

    plt.figure(figsize=(8,6))

    colors = [

        "green"
        if node in cover
        else "lightgray"

        for node in graph.nodes()
    ]

    nx.draw(
        graph,
        pos=positions,
        with_labels=True,
        node_color=colors,
        node_size=700
    )

    plt.title(title)

    plt.savefig(
        file_name,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()