def count_substring(string, sub_string):
    count = 0
    i = 0
    while i < len(string) - len(sub_string) + 1:
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
        i+=1
        
    return count
    
def count_substring_2(string, sub_string):
    count = 0
    start = 0
    
    while True:
        start = string.find(sub_string, start) + 1
        if start > 0:
            count += 1
        else:
            return start
    
    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
