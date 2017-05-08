# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

A = [int(i) for i in raw_input().split()]
B = [int(i) for i in raw_input().split()]

c = list(itertools.product(A,B))
output = ''
for item in c:
    output += str(item) + " "
    
print(output)
