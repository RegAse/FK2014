from math import sqrt
fj = int(input()) - 1
a,b = map(float,input().split())
total = 0
for i in range(fj):
	h,j = map(float,input().split())
	total += sqrt(pow(a - h,2) + pow(b - j,2))
	a,b = map(float,[h,j])
print(total)