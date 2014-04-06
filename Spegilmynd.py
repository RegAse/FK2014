height,width = [int(x) for x in input().split()]
fr = True
for x in range(height):
	li = input()
	for x in range(int(len(li)/2)):
		if li[x] != li[len(li)]:
			fr = False
if fr == True:
	print("Spegilmynd")
else:
	print("Ekki spegilmynd")