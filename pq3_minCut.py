__author__ = 'Lawrence'

import random


class UndirectedGraph(object):
    def __init__(self, filein):
        self.data = dict()
        with open(filein, 'r') as f:
            for ln in f:
                self.data[ln[0]] = ln[1:]

    def random_edge(self):
        weighted_vertices = [v for v in self.data for i in len(self.data[v])]
        v = random.choice(weighted_vertices)
        u = random.choice(self.data[v])
        return u, v




if __name__ == '__main__':
    main()