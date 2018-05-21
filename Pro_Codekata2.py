def leastdig():
	nv=input("Enter N Value:")
	kv=int(input("Enter K Value:"))
	list=[]
	for i in nv:
		list.append(i)
	list.sort()
	spc=''
	g=len(list)-kv
	for i in range(g):
		spc=spc+list[i]
	print(int(spc))
try:
	leastdig()
except:
	print('invalid')
