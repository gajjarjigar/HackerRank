if __name__ == '__main__':
    
    marksheet = list()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet.append([name, score])
    
    second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
    names = sorted([name for name,marks in marksheet if marks == second_highest])

    print(*names, sep='\n')
