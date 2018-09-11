from collections import OrderedDict

def merge_the_tools(s, k):
    print("\n".join(["".join(OrderedDict.fromkeys(s[i:i + k])) for i in range(0, len(s), k)]))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
