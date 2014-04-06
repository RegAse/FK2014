ord = input()
last = ""
final = ""
for x in ord:
    if x != last:
        final += x
    last = x
print(final)
input()