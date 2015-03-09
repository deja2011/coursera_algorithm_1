__author__ = 'Lawrence'

n = 875714
# n = 9
src = './.tmp/SCC.txt'
# src = './.tmp/SCC.mini.txt'

global_f = 0
fvalues = [0] * (n + 1)
sccs = [[] for ii in range(n + 1)]
visited_pass_1 = [0] * (n + 1)
visited_pass_2 = [0] * (n + 1)


def dfs_pass_1(graph, startpoint):
    global global_f
    global fvalues
    global visited_pass_1
    vstack = [startpoint]
    visited_pass_1[startpoint] = 1
    while vstack:
        cur = vstack.pop()
        if all([visited_pass_1[w] for w in graph[cur]]):
            global_f += 1
            if fvalues[cur]:
                raise Exception('fvalues %d = %d' % (cur, fvalues[cur]))
            fvalues[cur] = global_f
        else:
            vstack.append(cur)
            for v in filter(lambda vv: not visited_pass_1[vv], graph[cur]):
                vstack.append(v)
                visited_pass_1[v] = 1


def dfs_pass_1_rec(graph, v, depth):
    global global_f
    global fvalues
    global visited_pass_1
    global pass_1_highest
    if depth > pass_1_highest:
        pass_1_highest = depth
    visited_pass_1[v] = 1
    for w in graph[v]:
        if not visited_pass_1[w]:
            dfs_pass_1_rec(graph, w, depth + 1)
    global_f += 1
    fvalues[v] = global_f


def dfs_pass_2(graph, startpoint, leader):
    global visited_pass_2
    global sccs
    vstack = [startpoint]
    visited_pass_2[startpoint] = 1
    while vstack:
        cur = vstack.pop()
        for v in filter(lambda vv: not visited_pass_2[vv], graph[cur]):
            vstack.append(v)
            visited_pass_2[v] = 1
        sccs[leader].append(cur)


def dfs_pass_2_rec(graph, v, d, depth):
    global visited_pass_2
    global sccs
    global pass_2_highest
    if depth > pass_2_highest:
        pass_2_highest = depth
    visited_pass_2[v] = 1
    for w in graph[v]:
        if not visited_pass_2[w]:
            dfs_pass_2_rec(graph, w, d, depth + 1)
    sccs[d].append(v)


def main(*nkwargs, **kwargs):
    if nkwargs:
        print nkwargs
    if kwargs:
        print kwargs

    print 'Generating graph ...',
    graph = [[]]
    cur = 0
    with open(src, 'r') as dst:
        for ln in dst:
            tail, head = map(int, ln.strip().split())
            if tail == cur:
                graph[cur].append(head)
            else:
                # tail > cur
                for i in range(cur + 1, tail):
                    graph.append([])
                cur = tail
                graph.append([head])
    assert len(graph) == n + 1
    print 'DONE'

    print 'Generating graph_rev ...',
    graph_rev = list()
    for i in range(n + 1):
        graph_rev.append([])
    for i in range(1, n + 1):
        for j in graph[i]:
            graph_rev[j].append(i)
    assert len(graph_rev) == n + 1
    print 'DONE'

    print 'Proceeding the first pss DFS on graph_rev ...',
    for i in sorted(range(1, n + 1), reverse=False):
        if not visited_pass_1[i]:
            dfs_pass_1(graph_rev, i)
    print 'DONE'

    print 'Proceeding the second pass DFS on graph ...',
    for i in sorted(range(1, n + 1), reverse=True, key=lambda a: globals()['fvalues'][a]):
        if not visited_pass_2[i]:
            dfs_pass_2(graph, i, i)
    print 'DONE'

    print '(Lead Node : NO Nodes) of five larges SCCs are:'
    for k, v in sorted([(k, len(sccs[k])) for k in range(n + 1)], reverse=True, key=lambda t: t[1])[:6]:
        print k, v


if __name__ == '__main__':
    main()
