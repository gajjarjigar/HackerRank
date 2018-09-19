input()
a = set([int(value) for value in input().split()])
n = int(input())

[eval('a.{}({})'.format(input().split()[0], set([int(value) for value in input().split()]))) for _ in range(n)]
print(sum(a))
