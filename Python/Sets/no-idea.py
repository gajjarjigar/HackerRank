n,m = [int(value) for value in input().split()]
arr = [int(value) for value in input().split()]
set_a = set([int(value) for value in input().split()])
set_b = set([int(value) for value in input().split()])

print(sum((i in set_a)-(i in set_b) for i in arr))
