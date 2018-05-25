def oe():
	nof=int(input())
	arr=[]
	for i in range(nof):
		arr.append(int(input()))
	o,e=[],[]
	for i in range(nof):
		if i%2==0 and arr[i]%2!=0:
			o.append(arr[i])
		elif i%2!=0 and arr[i]%2==0:
			o.append(arr[i])
	print(o)
try:
	oe()
except:
	print('invalid')
