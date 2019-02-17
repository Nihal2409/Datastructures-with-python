#Selection Sort
# We keep iterating through the loop to find the smallest element and then swap it
# It runs in O(n2)

def selectionsort(A):
	i =0
	while i != len(A):
		min_value = A[i]		
		for j in range(i+1,len(A)):
			if A[j] < min_value:
				min_value = A[j]
				A[i], A[j] = A[j], A[i]
		i +=1
		
l = [9,8,7,6,5]
selectionsort(l)
print(l)
			