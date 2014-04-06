length = int(input())
li = [int(x) for x in input().split()]
to = True
for c in range(0,len(li) - 1):
	if li[c] >= li[c + 1]:
		to = False
		break
if to:
	print("Haekkandi")
else:
	print("Ekki haekkandi")
input()