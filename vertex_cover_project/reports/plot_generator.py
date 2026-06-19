import matplotlib.pyplot as plt

def plot_execution_time_comparison(
    devices,
    bf,
    bt,
    greedy,
    edge,
    file_name
):

    plt.figure(figsize=(10,6))

    plt.plot(
        devices,
        bf,
        marker="o",
        label="Brute Force"
    )

    plt.plot(
        devices,
        bt,
        marker="s",
        label="Backtracking"
    )

    plt.plot(
        devices,
        greedy,
        marker="^",
        label="Greedy"
    )

    plt.plot(
        devices,
        edge,
        marker="d",
        label="Edge-Greedy"
    )

    plt.title(
        "Execution Time Comparison"
    )

    plt.xlabel(
        "Number of Devices"
    )

    plt.ylabel(
        "Execution Time (ms)"
    )

    plt.grid(True)

    plt.legend()

    plt.savefig(
        file_name,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

def plot_vc_size_comparison(
    devices,
    bf,
    bt,
    greedy,
    edge,
    file_name
):

    plt.figure(figsize=(10,6))

    plt.plot(devices, bf, marker="o", label="Brute Force")
    plt.plot(devices, bt, marker="s", label="Backtracking")
    plt.plot(devices, greedy, marker="^", label="Greedy")
    plt.plot(devices, edge, marker="d", label="Edge-Greedy")

    plt.title(
        "Vertex Cover Size Comparison"
    )

    plt.xlabel(
        "Number of Devices"
    )

    plt.ylabel(
        "Vertex Cover Size"
    )

    plt.grid(True)

    plt.legend()

    plt.savefig(
        file_name,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

def plot_error_comparison(
    devices,
    greedy,
    edge,
    file_name
):

    plt.figure(figsize=(10,6))

    plt.plot(
        devices,
        greedy,
        marker="^",
        label="Greedy"
    )

    plt.plot(
        devices,
        edge,
        marker="d",
        label="Edge-Greedy"
    )

    plt.title(
        "Error Percentage Comparison"
    )

    plt.xlabel(
        "Number of Devices"
    )

    plt.ylabel(
        "Error (%)"
    )

    plt.grid(True)

    plt.legend()

    plt.savefig(
        file_name,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

def plot_approximation_comparison(
    devices,
    greedy,
    edge,
    file_name
):

    plt.figure(figsize=(10,6))

    plt.plot(
        devices,
        greedy,
        marker="^",
        label="Greedy"
    )

    plt.plot(
        devices,
        edge,
        marker="d",
        label="Edge-Greedy"
    )

    plt.title(
        "Approximation Ratio Comparison"
    )

    plt.xlabel(
        "Number of Devices"
    )

    plt.ylabel(
        "Approximation Ratio"
    )

    plt.grid(True)

    plt.legend()

    plt.savefig(
        file_name,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

def plot_energy_comparison(
    devices,
    bf,
    bt,
    greedy,
    edge,
    file_name
):

    plt.figure(figsize=(10,6))

    plt.plot(devices, bf, marker="o", label="Brute Force")
    plt.plot(devices, bt, marker="s", label="Backtracking")
    plt.plot(devices, greedy, marker="^", label="Greedy")
    plt.plot(devices, edge, marker="d", label="Edge-Greedy")

    plt.title(
        "Energy Saving Comparison"
    )

    plt.xlabel(
        "Number of Devices"
    )

    plt.ylabel(
        "Energy Saving (%)"
    )

    plt.grid(True)

    plt.legend()

    plt.savefig(
        file_name,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()