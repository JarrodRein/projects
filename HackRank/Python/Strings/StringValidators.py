if __name__ == '__main__':
    s = input()
    for i in range(0, len(s)):
        if s[i].isalnum():
            print("True")
        else:
            print("False")
        break
    for i in range(0, len(s)):
            if s[i].isalpha():
                print("True")
            else:
                print("False")
            break
    #print(s.isalnum())
   # print(s.isalpha())
    for i in range(0, len(s)):
                if s[i].isdigit():
                    print("False")
                else:
                    print("True")
                break
   
   # print(s.isdigit())
   # print(s.islower())
    for i in range(0, len(s)):
            if s[i].islower():
                print("True")
            else:
                print("False")
            break
    #print(s.isupper())
    
    for i in range(0, len(s)):
            if s[i].isupper():
                print("False")
            else:
                print("True")
            break