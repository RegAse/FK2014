raw = input().split()
width = int(raw[0])
height = int(raw[1])
ar = []
san = width + 1
li = [""] * san
od = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z"}
for i in range(height):
	for x in input():
		ar.append(x)
ar.append("B")
count = 1
for row in range(0,(width * 2),2):
	r = row
	c = count
	letter = od[c]
	for col in range(0,height):
		if r != 0:
			if ar[r + 1] == "-":
				r += 2
				c += 1
			elif ar[r - 1] == "-":
				r -= 2
				c -= 1
		elif r == 0:
			if ar[r + 1] == "-":
				r += 2
				c += 1
		r += (width + width - 1)
	count += 1
	li[c] = letter
print(''.join(li))
input()