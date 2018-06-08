from collections import deque
#list rotation
def rotate(arr,k):
	brr=deque(arr)
	brr.rotate(k)
	print('rotation of the list k times:',brr)
def sum_list(arr):
	print('sum of the list:',sum(arr))
	
print('enter the size of list')
n=int(input())
arr=list(map(int,input().strip().split(' ')))
print('enter the no. of rotation:')
k=int(input())
rotate(arr,k)
sum_list(arr)


