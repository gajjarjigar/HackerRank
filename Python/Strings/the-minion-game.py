def minion_game(string):
    vowels = 'AEIOU'
    
    stuart_score = 0
    kevin_score = 0
    
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score = kevin_score + len(string) - i
        else:
            stuart_score = stuart_score + len(string) - i
            
    if kevin_score > stuart_score:
        print('Kevin ' + str(kevin_score))
    elif kevin_score < stuart_score:
        print('Stuart ' + str(stuart_score))
    else:
        print('Draw')
    
if __name__ == '__main__':
    s = input()
    minion_game(s)
