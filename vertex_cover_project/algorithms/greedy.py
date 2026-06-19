def solve(edges):

    edges = set(edges)

    cover = set()

    while edges:

        degree = {}

        for u, v in edges:

            degree[u] = degree.get(u, 0) + 1
            degree[v] = degree.get(v, 0) + 1

        best = max(
            degree,
            key=degree.get
        )

        cover.add(best)

        edges = {
            (u, v)
            for u, v in edges
            if u != best and v != best
        }

    return {
        "cover": cover
    }