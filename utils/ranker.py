# ranker.py
from datatypes.sets import Set
from datatypes.result import Result


class Ranker:
    def __init__(self, graph, itermax=100, d=0.85):
        self._ranks = {}
        self._backlinks = {}
        self._L = {}
        self._init_rank(graph, itermax, d)

    def _init_rank(self, graph, itermax, d):
        # NOTE(Jovan): Inicijalizuju se vrednosti na pocetku
        # kako se ne bi morale racunati za svako rangiranje
        self._backlinks = graph.backlinks
        N = graph.vertex_count()
        factor = (1.0 - d) / N
        for v in graph.vertices():
            path = v.path
            self._ranks[path] = 1.0 / N
            self._L[path] = len(v.links)

        # NOTE(Jovan): Iterativno odredjivanje PageRank-a
        # NOTE(Jovan): pi - trenutna, pj - backlink
        for _ in range(itermax):
            new_ranks = {}
            for pi in self._ranks:
                new_ranks[pi] = factor
                # NOTE(Jovan) sum(PR(pj) / L(pj))
                for pj in self._backlinks[pi]:
                    new_ranks[pi] += d * (self._ranks[pj] / self._L[pj])
            self._ranks = new_ranks

    # NOTE(Jovan): Funkcija za racunanje ranga
    def rank_pages(self, pages):
        res = Set()
        pages = dict(zip([p.path for p in pages],
                         [p.count for p in pages]))
        # NOTE(Jovan): Uticaj PR-a na rank, empirisjki odrediti
        PR_WEIGHT = 1.0 / 3.0
        # NOTE(Jovan): Uticaj backlinkova sa trazenim upitom
        BL_WEIGHT = 1.0 / 3.0
        for r in pages:
            c = pages[r]
            blsum = sum([pages.get(i, 0) for i in self._backlinks[r]])
            if c != 0:
                rank = (pages[r] * (1 + self._ranks[r] * PR_WEIGHT)
                        + blsum * BL_WEIGHT)
            else:
                rank = self._ranks[r]
            res.add(Result(r, rank))
        return res
