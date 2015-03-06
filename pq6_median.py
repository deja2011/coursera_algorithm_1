__author__ = 'Lawrence Li'

import heapq

class Source(object):

    def __init__(self, fname):
        self.fid = open(fname, 'r')

    def __iter__(self):
        for ln in self.fid:
            yield int(ln[:-1])

    def __del__(self):
        self.fid.close()


def main(*nkwargs, **kwargs):
    if nkwargs:
        print nkwargs
    if kwargs:
        print kwargs

    litend = list()
    bigend = list()
    medians = list()

    for v in Source('Median.txt'):
        if (not litend) or v <= -litend[0]:
            heapq.heappush(litend, -v)
        else:
            heapq.heappush(bigend, v)
        if len(litend) > len(bigend) + 1:
            heapq.heappush(bigend, -heapq.heappop(litend))
        elif len(litend) < len(bigend) - 1:
            heapq.heappush(litend, -heapq.heappop(bigend))
        else:
            pass
        # print litend, bigend

        if len(litend) >= len(bigend):
            medians.append(-litend[0])
        else:
            medians.append(bigend[0])

    # print medians
    print sum(medians)



if __name__ == '__main__':
    main()
