# ranker.py
from sets import Set


# NOTE(Jovan): Sluzi za prikazivanje rezultata pretrage
class RankResult:
    slots = ['_path', '_score']

    def __init__(self, path, score=None):
        self._path = path
        self._score = 0 if score is None else score

    def get_path(self):
        return self._path

    def get_score(self):
        return self._score

    def __iadd__(self, other):
        if other == self:
            self._score += other._score
            return self

    def __str__(self):
        return self._path + ': ' + str(self._score)

    def __eq__(self, other):
        return isinstance(other, RankResult) and self._path == other._path

    def __hash__(self):
        return hash(self._path)


# NOTE(Jovan): Funkcija za racunanje ranga
def rank_pages(graph, pages, d=0.85, iter_max=100):
    ranks = {}
    N = graph.vertex_count()
    backlinks = {}
    # NOTE(Jovan): Damping factor
    factor = (1.0 - d) / N
    L = {}
    # NOTE(Jovan): Inicijalne vrednosti
    for p in pages:
        path = p.get_path()
        ranks[path] = 1.0 / N
        backlinks[path] = graph.get_backlink(graph.get_vertex(path))
        L[path] = len(graph._vertices[path].get_links())
    # NOTE(Jovan): Iterativno odredjivanje PageRank-a
    # NOTE(Jovan): pi - renutna, pj - backlink
    for _ in range(iter_max):
        new_ranks = {}
        for pi in ranks:
            new_ranks[pi] = factor
            # NOTE(Jovan) sum(PR(pj) / L(pj))
            for pj in backlinks[pi]:
                new_ranks[pi] += d * (ranks[pj] / L[pj])
        ranks = new_ranks
    res = Set()
    pages = dict(zip([p.get_path() for p in pages], [p.get_count() for p in pages]))
    # NOTE(Jovan): Uticaj PR-a na rank, empirisjki odrediti
    PR_WEIGHT = 1.0 / 3.0
    for r in ranks:
        rank = pages[r] * (1 + (ranks[r] - 1) * PR_WEIGHT)
        res.add(RankResult(r, rank))
    return res
