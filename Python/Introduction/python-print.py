if __name__ == '__main__':
    n = int(input())
    print(*(range(1,n+1)), sep='')
    
    '''
      * ==> unpacking operator
      
      print([1,2,3])
      ==> [1, 2, 3]

      print(*[1,2,3])
      ==> 1 2 3

      print(1,2,3)
      ==> 1 2 3
    
    '''
