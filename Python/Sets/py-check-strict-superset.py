a = set(input().split())
n = int(input())

is_it = True

for _ in range(n):
    b = set(input().split())
    if not(len(a-b) + len(a) > len(b) and len((b-a)) == 0):
        is_it = False
        break
        

print(is_it)
