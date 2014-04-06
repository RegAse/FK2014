x = int(input())
print(x,"! = ",sep="",end="")
for y in range(1,x + 1):
	if x == y:
		print(y,end="")
	else:
		print(y,"x ",end="")
input()