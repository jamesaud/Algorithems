# takes a sorted list
#https://www.hackerrank.com/challenges/find-the-running-median
import bisect
# Enter your code here. Read input from STDIN. Print output to STDOUT

def middle(ls):
    n = len(ls)
    m = n - 1
    return (ls[n/2] + ls[m/2]) / 2.0

ls = []
for _ in range(int(raw_input())):
    n = int(raw_input())
    bisect.insort(ls, n)
    print(middle(ls))
