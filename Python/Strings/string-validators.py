if __name__ == '__main__':
    s = input()
    
    alphanumeric = False
    alphabetical = False
    digits = False
    lowercase = False
    uppercase = False
    
    for c in s:
        if c.islower():
            lowercase = True
        if c.isupper():
            uppercase = True
        if c.isdigit():
            digits = True
            alphanumeric = True
        if c.isalpha():
            alphabetical = True
            alphanumeric = True
    
    
    print(alphanumeric)
    print(alphabetical)
    print(digits)
    print(lowercase)
    print(uppercase)

    
