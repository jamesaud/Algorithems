# Enter your code here. Read input from STDIN. Print output to STDOUT
sum, startIndex = 0, 0
n = int(raw_input())

for i in range(n):
    p,d = map(int,raw_input().split())
    sum += p - d
    if sum < 0:
        sum = 0
        startIndex = i + 1
print(startIndex)
