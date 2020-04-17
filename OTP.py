def main():
    x = input('Enter message: ')
    y = input('Enter coded text: ')
    x = x.lower()
    y = y.lower()
    i = 0
    ret = ""
    if len(x) == len(y):
        while i < len(x):
            if ord(x[i]) < ord(y[i]):
                new = ord(y[i]) - ord(x[i]) + 96
                ret = str(ret) + chr(new)
                i+=1
            else:
                new = ord(y[i]) - ord(x[i]) + 26 + 96
                ret = str(ret) + chr(new)
                i+=1
    
    print(ret)
main()