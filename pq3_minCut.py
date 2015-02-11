__author__ = 'Lawrence'

import random, operator, sys


class UndirectedGraph(object):
    def __init__(self, filein):
        self.data = dict()
        with open(filein, 'r') as f:
            for ln in f:
                ln = ln.split()
                self.data[int(ln[0])] = map(int, ln[1:])

    def random_edge(self):
        weighted_vertices = [v for v in self.data for i in range(len(self.data[v]))]
        v = random.choice(weighted_vertices)
        u = random.choice(self.data[v])
        return u, v

    def merge(self, u, w):
        self.data[u] = filter(lambda n: n not in (u, w), self.data[u] + self.data[w])
        for v in (set(self.data) - {u, w}):
            self.data[v] = map(lambda n: u if n == w else n, self.data[v])
        del self.data[w]
        assert (w not in self.data.keys())
        assert (w not in reduce(operator.add, self.data.values()))

    def __repr__(self):
        # return '\n'.join(map(lambda i: '{0:3}:{1}'.format(*i), self.data.items()))
        ne = sum(map(len, self.data.values())) / 2
        nv = len(self.data)
        return '#V:{0:8}, #E:{1:8}'.format(nv, ne)

    def __len__(self):
        return len(self.data)

    def noedges(self):
        return sum(map(len, self.data.values())) / 2


def attempt():
    ug = UndirectedGraph('./kargerMinCut.txt')
    while len(ug) > 2:
        ug.merge(*ug.random_edge())
    return ug.noedges()


def main(*nkwargs, **kwargs):
    if nkwargs:
        print nkwargs
    if kwargs:
        print kwargs

    TRIALS = 1000

    res = list()
    for i in range(TRIALS):
        sys.stdout.write('\r{0:5} of {1}'.format(i, TRIALS))
        sys.stdout.flush()
        res.append(attempt())
    sys.stdout.write('\n')

    print min(res)


if __name__ == '__main__':
    main()