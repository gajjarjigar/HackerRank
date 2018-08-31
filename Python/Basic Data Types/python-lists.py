if __name__ == '__main__':
    N = int(input())
    a = list()
    for _ in range(N):
        statement = input().split()
        if statement[0] == 'print':
            print(a)
        else:
            eval('a.{}'.format(statement[0]) + '({})'.format(','.join(statement[1:len(statement)])))
