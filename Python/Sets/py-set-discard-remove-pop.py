n = int(input())
s = set(map(int, input().split()))
c = int(input())

for _ in range(c):
    eval('s.{}({})'.format(*input().split() + [''] ))
    
print(sum(s))
