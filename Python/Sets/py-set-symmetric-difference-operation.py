a,b = [input().split() for _ in range(4)][1::2]
print(len(set(a) ^ set(b)))
