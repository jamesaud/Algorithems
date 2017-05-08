from __future__ import print_function
#https://www.hackerrank.com/challenges/equal-stacks
#!/bin/python

import sys


n1,n2,n3 = raw_input().strip().split(' ')

h1 = map(int, raw_input().strip().split(' '))
h2 = map(int, raw_input().strip().split(' '))
h3 = map(int, raw_input().strip().split(' '))
h1.reverse()
h2.reverse()
h3.reverse()

h1_sum, h2_sum, h3_sum = sum(h1), sum(h2), sum(h3)

while h1_sum != h2_sum or h2_sum != h3_sum:
    largest = max(h1_sum, h2_sum, h3_sum)
    if largest == h1_sum:
        h1_sum -= h1.pop()
    elif largest == h2_sum:
        h2_sum -= h2.pop()
    else:
        h3_sum -= h3.pop()
           
print(h1_sum)
