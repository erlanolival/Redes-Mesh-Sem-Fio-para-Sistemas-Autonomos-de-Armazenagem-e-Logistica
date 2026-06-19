def solve(edges):

    edges = set(edges)

    cover = set()

    while edges:

        u, v = next(iter(edges))

        cover.add(u)
        cover.add(v)

        edges = {
            (a, b)
            for a, b in edges
            if (
                a != u and
                b != u and
                a != v and
                b != v
            )
        }

    return {
        "cover": cover
    }