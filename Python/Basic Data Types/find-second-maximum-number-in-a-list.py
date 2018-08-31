import math

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    max = -math.inf
    second_max = -math.inf
    count = 0
    for i in arr:
        count+=1
        if i > second_max:
            if i > max:
                max, second_max = i, max
            elif i == max:
                pass
            else:
                second_max = i
    
    print(second_max if count >= 2 else None)
