from __future__ import print_function

# https://www.hackerrank.com/challenges/missing-numbers
# Missing Numbers

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

a = raw_input()
l1 = raw_input().split(' ')
b = raw_input()
l2 = raw_input().split(' ')

def find_missing(l1, l2):
    l1_dict = defaultdict(lambda : 0)
    l2_dict = defaultdict(lambda : 0)
    missing_nums = []
    
    for item in l1:
        l1_dict[item] += 1    
    for item in l2:
        l2_dict[item] += 1

    for item in l1_dict:
        if l1_dict.get(item) != l2_dict.get(item):
            missing_nums.append(item)
    return missing_nums
            
nums = find_missing(l1,l2)
nums.sort()
for num in nums:
    print(num, end=' ')
