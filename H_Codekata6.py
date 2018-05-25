def rpt(arr):
	for i in range(len(arr)):
		for j in range(i+1,len(arr)):
			if arr[i]==arr[j]:
				return arr[i]
	return 'Unique'
def main():
	nof=int(input())
	arr=[]
	for i in range(nof):
		arr.append(int(input()))
	print(rpt(arr))
try:
	main()
except:
	print('invalid')
