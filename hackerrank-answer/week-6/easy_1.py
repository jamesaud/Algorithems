from __future__ import print_function

# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/array-left-rotation
rotations = int(raw_input().split()[1])
ls = raw_input().split()
rotations = rotations % len(ls)
start_shift = ls[rotations:]
end_shift = ls[:rotations]

start_shift += end_shift
for item in start_shift:
    print (item, end=' ')
