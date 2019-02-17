# Merge Sort Algorithm
# It is a recursive approach here
# Divide and Conquer type
# Very efficient for large datasets
# Merge Sort does log n merge steps because each merge step doubles the list size
# it does n work for each merge step because it must look at every items
# so it runs in O(n log n)
import sys
def mergesort(A):
	merge_sort2(A,0,len(A)-1)
	
def merge_sort2(A,first,last):
	if first < last:
		middle = (first+last)//2
		merge_sort2(A,first,middle)
		merge_sort2(A,middle+1,last)
		merge(A,first,middle,last)
		
def merge(A,first,middle,last):
	L = A[first:middle+1]
	R = A[middle+1:last+1]
	L.append(sys.maxsize)
	R.append(sys.maxsize)
	i = j = 0
	for k in range(first,last+1):
		if L[i] <= R[j]:
			A[k] = L[i]
			i+=1
		else:
			A[k] = R[j]
			j +=1
			
l =[9,8,7,6,5,4]
mergesort(l)
print(l)