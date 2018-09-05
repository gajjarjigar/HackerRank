def wrap_2(string, max_width):
    s = ''
    i = 0
    while True:
        if i+max_width <= len(string):
            s = s + string[i:i+max_width] + '\n'
            i = i+max_width
        else:
            s = s + string[i:]
            break
        
    return s

def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string,max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
