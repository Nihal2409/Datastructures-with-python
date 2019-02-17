# 2 7 6 3 9
# Insertion involves swapping of elements when it meets a condition
# swapping is a little expensive so we use overwriting technique

def insertionsort(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum

l = [9,7,8,6,5]
insertionsort(l)
print(l)