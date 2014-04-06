n = int(input())
for i in range(0, n):
	if(i % 2 == 0):
		for x in range(0, n):
			if(x % 2 == 0 ): print("H", end="")
			else: print("S", end="")
		print()
	else:
		for e in range(0, n):
			if(e % 2 == 0 ): print("S", end="")
			else: print("H", end="")
		print()
input()