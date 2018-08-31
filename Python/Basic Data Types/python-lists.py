if __name__ == '__main__':
    N = int(input())
    a = list()
    for _ in range(N):
        statement = input().split()
        if statement[0] == 'print':
            print(a)
        else:
            command = statement[0]
            args = ','.join(statement[1:len(statement)])
            eval('a.{}({})'.format(command,args))
