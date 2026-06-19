def solve(edges, n):

    best_cover = set(range(n))

    def backtrack(
        remaining_edges,
        cover
    ):

        nonlocal best_cover

        if len(cover) >= len(best_cover):
            return

        if not remaining_edges:

            best_cover = cover.copy()
            return

        u, v = next(iter(remaining_edges))

        edges_u = {
            e
            for e in remaining_edges
            if u not in e
        }

        cover.add(u)

        backtrack(
            edges_u,
            cover
        )

        cover.remove(u)

        edges_v = {
            e
            for e in remaining_edges
            if v not in e
        }

        cover.add(v)

        backtrack(
            edges_v,
            cover
        )

        cover.remove(v)

    backtrack(
        set(edges),
        set()
    )

    return {
        "cover": best_cover
    }