import itertools

def is_vertex_cover(subset, edges):

    cover = set(subset)

    for u, v in edges:

        if u not in cover and v not in cover:
            return False

    return True


def solve(edges, n):

    nodes = list(range(n))

    subsets = 0

    for k in range(n + 1):

        for subset in itertools.combinations(nodes, k):

            subsets += 1

            if is_vertex_cover(subset, edges):

                return {
                    "cover": set(subset),
                    "subsets": subsets
                }

    return {
        "cover": set(),
        "subsets": subsets
    }