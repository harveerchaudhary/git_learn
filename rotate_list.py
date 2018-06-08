from collections import deque
def rotate(arr,k):
	brr=deque(arr)
	brr.rotate(k)
	print(brr)
print('enter the size of list')
n=int(input())
arr=list(map(int,input().strip().split(' ')))
print('enter the no. of rotation:')
k=int(input())
rotate(arr,k)
