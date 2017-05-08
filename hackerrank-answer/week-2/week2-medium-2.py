# https://www.hackerrank.com/challenges/angry-children
# Max - Min

import sys

N = input()
K = input()
num_list = [input() for _ in range(N)]

def find_unfairness(k, l1):
    l1.sort()
    unfairness = sys.maxint
    for i in range(len(l1) - k + 1):
        difference = abs(l1[i+k-1] - l1[i])
        if difference < unfairness:
            unfairness = difference

    print(unfairness)

find_unfairness(K, num_list)
