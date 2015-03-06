__author__ = 'Lawrence Li'


def sortmethod(array):
    array.sort()


def selectmethod(array):
    length = len(array)
    ret = list()
    for ii in range(length):
        left = array[ii]
        for jj in range(ii + 1, length):
            total = left + array[jj]
            if -10000 <= total <= 10000:
                ret.append(total)
                break
        print '\r%d' % int(float(ii) / 20001 * 100),
    return len(set(ret))


def hashmethod(array):
    cnt = 0
    for i in xrange(-10000, 10001):
        for ele in array:
            diff = i - ele
            if diff != ele and diff in array:
                cnt += 1
                break
        print '\r%d' % int(float(i) / 20001 * 100),
    print cnt


def main():
    method = sortmethod
    print method([int(ln[:-1]) for ln in open('algo1_programming_prob_2sum.txt', 'r')])


if __name__ == '__main__':
    main()
