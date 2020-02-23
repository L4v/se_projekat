# ranker.py
from datatypes.sets import Set
from datatypes.result import Result


# NOTE(Jovan): Funkcija za racunanje ranga
def rank_pages(graph, pages, d=0.85, iter_max=100):
    # NOTE(Jovan): Cuvaju se svi rangovi
    ranks = {}
    # NOTE(Jovan): Ukupan broj linkova
    N = graph.vertex_count()
    # NOTE(Jovan): Povratni linkovi
    backlinks = {}
    # NOTE(Jovan): Damping factor
    factor = (1.0 - d) / N
    # NOTE(Jovan): Broj linkova po stranici
    L = {}

    # NOTE(Jovan): Inicijalne vrednosti
    for v in graph.vertices():
        path = v.path
        ranks[path] = 1.0 / N
        backlinks[path] = graph.get_backlink(v.path)
        L[path] = len(v.links)

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
    for r in pages:
        c = pages[r]
        blsum = sum([pages.get(i, 0) for i in backlinks[r]])
        if c != 0:
            rank = pages[r] * (1 + ranks[r] * PR_WEIGHT) + blsum * BL_WEIGHT
        else:
            rank = ranks[r]
        res.add(Result(r, rank))
    return res
