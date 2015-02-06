__author__ = 'Lawrence'

import random


def qsort(array, start, end, method, side):
    if start >= end:
        return 0
    pidx, pval = method(array, start, end)
    if pidx != start:
        array[start], array[pidx] = array[pidx], array[start]
    i = start + 1
    j = start + 1
    count = end - start
    while j <= end:
        if array[j] < pval:
            array[i], array[j] = array[j], array[i]
            i += 1
        j += 1
    array[start], array[i-1] = array[i-1], array[start]
    # print array, start, end, pidx, pval, i, side
    count += qsort(array, start, i-2, method, side+'L')
    count += qsort(array, i, end, method, side+'R')
    return count


def pivot_1(array, start, end):
    return start, array[start]


def pivot_2(array, start, end):
    return end, array[end]


def pivot_3(array, start, end):
    if (end - start) % 2:
        # even number of elements
        # 3 4 5 6 7 8
        mid = start + (end - 1 - start) / 2
    else:
        mid = start + (end - start) / 2
    retidx = sorted((start, mid, end), key=lambda i: array[i])[1]
    return retidx, array[retidx]


def main():
    # array = range(1, 9)
    # random.shuffle(array)
    # array = [3, 8, 2, 5, 1, 4, 7, 6]
    array = map(int, open('QuickSort.txt', 'r').readlines())
    # print len(array), array[0], array[-1], array[3]
    # return
    # print array
    array = map(int, open('QuickSort.txt', 'r').readlines())
    print qsort(array, 0, len(array)-1, pivot_1, 'M')
    array = map(int, open('QuickSort.txt', 'r').readlines())
    print qsort(array, 0, len(array)-1, pivot_2, 'M')
    array = map(int, open('QuickSort.txt', 'r').readlines())
    print qsort(array, 0, len(array)-1, pivot_3, 'M')
    # print array


def test():
    for i in range(5, 11):
        array = range(i)
        random.shuffle(array)
        print ''
        print array
        print pivot_3(array, 0, i-1)


if __name__ == '__main__':
    main()
    # test()
