if __name__ == '__main__':
    x = int(input())+1
    y = int(input())+1
    z = int(input())+1
    n = int(input())
    
    output = [[x_i,y_i,z_i] for x_i in range(x) for y_i in range(y) for z_i in range(z) if x_i + y_i + z_i != n]
    
    print(output)
