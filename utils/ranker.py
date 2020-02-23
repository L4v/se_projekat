# ranker.py
from datatypes.sets import Set
from datatypes.result import Result


# NOTE(Jovan): Funkcija za racunanje ranga
def rank_pages(graph, pages, d=0.85, iter_max=100):
    ranks = {}
    N = graph.vertex_count()
    backlinks = {}
    # NOTE(Jovan): Damping factor
    factor = (1.0 - d) / N
    # NOTE(Jovan): Broj linkova u odredjenoj stranici
    L = {}
    # NOTE(Jovan): Inicijalne vrednosti
    for p in pages:
        path = p.path
        ranks[path] = 1.0 / N
        backlinks[path] = graph.get_backlink(graph.get_vertex(path, as_path=True))
        L[path] = len(graph._vertices[path].links)
    # NOTE(Jovan): Iterativno odredjivanje PageRank-a
    # NOTE(Jovan): pi - trenutna, pj - backlink
    for _ in range(iter_max):
        new_ranks = {}
        for pi in ranks:
            new_ranks[pi] = factor
            # NOTE(Jovan) sum(PR(pj) / L(pj))
            for pj in backlinks[pi]:
                new_ranks[pi] += d * (ranks[pj] / L[pj])
        ranks = new_ranks
    res = Set()
    pages = dict(zip([p.path for p in pages],
                     [p.count for p in pages]))
    # NOTE(Jovan): Uticaj PR-a na rank, empirisjki odrediti
    PR_WEIGHT = 1.0 / 3.0
    # NOTE(Jovan): Uticaj backlinkova sa trazenim upitom
    BL_WEIGHT = 1.0 / 3.0
    for r in ranks:
        rank = pages[r] * (
                           1
                           + (ranks[r] - 1) * PR_WEIGHT
                           + len(backlinks[r]) * BL_WEIGHT)
        res.add(Result(r, rank))
    return res
