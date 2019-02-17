#Bubble sorting technique
# In this sort maximum element is bubbled to the last of the list hence the name Bubble sort
# O(n2)

def bubblesort(A):
	for i in range(0,len(A)-1):
		for j in range(0,len(A)-1-i):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
				
l = [9,8,7,6,5,4]
bubblesort(l)
print(l)