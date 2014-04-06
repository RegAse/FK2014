word = input()
for i in word:
    if(str.isupper(i)): print(i.lower(), end="")
    else : print(i.upper(), end="")
input()