n=int(input())
m=[]
while(n<1 or n>10000):
	print(f'number ={n},  The number must be between 1 and 10000')
	n=int(input())
for i in range(n):
	m.append(int(input()))
m.reverse()
print(m)
