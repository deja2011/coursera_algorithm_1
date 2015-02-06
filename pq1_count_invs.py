__author__ = 'Lawrence'

import random, sys


def merge(lleft, lright, n):
    # print 'Left :', lleft
    # print 'Right:', lright
    # print 'Total:', n
    ret = list()
    lenleft = len(lleft)
    i = 0
    j = 0
    inv = 0
    for k in range(n):
        if i == len(lleft):
            ret.append(lright[j])
            j += 1
        elif j == len(lright):
            ret.append(lleft[i])
            i += 1
        elif lleft[i] < lright[j]:
            ret.append(lleft[i])
            i += 1
        else:
            ret.append(lright[j])
            j += 1
            inv += (lenleft - i)
    return ret, inv


def msort(array):
    if len(array) == 1:
        return array, 0
    else:
        half = len(array) / 2
        # print array[:half]
        # print array[half:]
        try:
            lleft, invleft = msort(array[:half])
        except ValueError as e:
            print array, half
            sys.exit(1)
            raise e
        lright, invright = msort(array[half:])
        ret, invnew = merge(lleft, lright, len(array))
        return ret, invleft + invright + invnew


def main():
    array = range(6)
    array = [6] + array
    array[-3], array[-1] = array[-1], array[-3]
    # random.shuffle(array)
    array = map(int, open('IntegerArray.txt', 'r').readlines())
    # print array[0], array[-1], array[3]
    # return
    # print array
    ret, inv = msort(array)
    # print ret
    print len(ret)
    print inv


if __name__ == '__main__':
    main()
