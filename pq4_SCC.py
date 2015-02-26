__author__ = 'Lawrence'


def main(*nkwargs, **kwargs):
    if nkwargs:
        print nkwargs
    if kwargs:
        print kwargs

    print 'Generating graph'

    graph = [[]]
    cur = 0
    with open('./.tmp/SCC.txt', 'r') as dst:
        for ln in dst:
            tail, head = map(int, ln[:-1].split())
            if tail == cur:
                try:
                    graph[cur].append(head)
                except IndexError as e:
                    raise e
            elif tail > cur:
                for i in range(cur + 1, tail):
                    graph.append([])
                cur = tail
                graph.append([head])
            else:
                raise Exception, 'Invalid tail %d and cur %d.' % (tail, cur)

    print len(graph)
    print graph[0]
    print graph[1]
    print graph[20]
    print graph[875714]

    print 'Generating graph_rev'

    graph_rev = list()
    for i in range(len(graph)):
        graph_rev.append([])
    for i in range(1, len(graph)):
        for j in graph[i]:
            graph_rev[j].append(i)

    print len(graph_rev)
    print graph_rev[0]
    print graph_rev[1]
    print graph_rev[20]
    print graph_rev[875714]

    print 'Proceeding the first DFS on graph_rev'


if __name__ == '__main__':
    main()
