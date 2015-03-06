__author__ = 'Lawrence'

from heapq import heapify, heappush, heappop

MAXLENGTH = 1000000
REQUIRED = (7, 37, 59, 82, 99, 115, 133, 165, 188, 197)

def heapupdate(heap, item, key):
    idx = 0
    while idx < len(heap):
        if heap[idx][-1] == item:
            heap[idx][0] = key
            heapify(heap)
            return 1
        idx += 1
    raise KeyError('cannot find %s in %s' % (item, heap))


def main(*nkwargs, **kwargs):
    if nkwargs:
        print nkwargs
    if kwargs:
        print kwargs

    graph = [[]]
    with open('dijkstraData.txt', 'r') as src:
        for ln in src:
            graph.append(map(lambda s: map(int, s.split(',')), ln.split()[1:]))

    uncaled = [[MAXLENGTH, v] for v in range(2, 201)]
    dist = [MAXLENGTH] + [0] + [MAXLENGTH] * 199
    for v, len_1v in graph[1]:
        uncaled.remove([MAXLENGTH, v])
        uncaled.append([len_1v, v])
        dist[v] = len_1v
    heapify(uncaled)

    caled = [[0, MAXLENGTH], [1, 0]]

    while uncaled:
        # v: the node to add to collection caled.
        # w: each node connected to v directly.
        # print 'picked %d from uncalculated collection.' % v
        d, v = heappop(uncaled)
        caled.append([v, dist[v]])
        for w, len_vw in graph[v]:
            if w not in [li[0] for li in caled] and dist[w] > dist[v] + len_vw:
                dist[w] = dist[v] + len_vw
                heapupdate(uncaled, w, dist[w])
                # print '    updated %d in uncalculated collection from %d to %d. ADD:%s' % \
                #       (w, dist[w], dist[v] + len_vw, 108 in [s[-1] for s in uncaled])

    print len(caled)

    for v in (0, 1, 2, 92, 170) + REQUIRED:
        print v, dist[v]

    print ','.join([str(dist[v]) for v in REQUIRED])

if __name__ == '__main__':
    main()
