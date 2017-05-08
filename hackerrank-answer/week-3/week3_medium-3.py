def pairs(a,k):
    s = set(a)
    tot = 0

    for x in s:
        if x+k in s:
            tot += 1
     
    return tot

k = int(raw_input().split()[1])
a = [int(item) for item in raw_input().split()]
print(pairs(a,k))
