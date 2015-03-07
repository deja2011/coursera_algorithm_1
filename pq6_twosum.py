__author__ = 'Lawrence Li'

import multiprocessing


class CalTwoSum(multiprocessing.Process):

    def __init__(self, begin, end, array):
        multiprocessing.Process.__init__(self)
        self.iter = xrange(begin, end + 1)
        self.array = array
        self.cnt = 0

    def run(self):
        is2sum = self.is2sum
        for t in self.iter:
            if is2sum(t):
                self.cnt += 1

    def is2sum(self, t):
        s = self.array
        for ele in s:
            diff = t - ele
            if diff != ele and diff in s:
                return True
        else:
            return False


def hashmethod(array):
    cnt = 0
    for t in xrange(-10000, 10001):
        if is2sum(t, array):
            cnt += 1
        print '\r%d' % t,
    return cnt


def main():

    start, end, np = -10000, 10000, 10
    array = set([int(ln[:-1]) for ln in open('algo1_programming_prob_2sum.txt', 'r')])

    unit = abs(start - end) / np
    starts = [(start + n * unit) for n in range(np)]
    ends = [(start + n * unit + unit - 1) for n in range(np)]
    ends[-1] = end + 2

    plist = list()
    cnt = 0
    # print zip(starts, ends)

    for s, e in zip(starts, ends):
        p = CalTwoSum(s, e, array)
        plist.append(p)

    for p in plist:
        p.start()

    for p in plist:
        p.join()
        cnt += p.cnt

    print cnt

    # print len(array)
    # print method([int(ln[:-1]) for ln in open('algo1_programming_prob_2sum.txt', 'r')])


if __name__ == '__main__':
    main()
