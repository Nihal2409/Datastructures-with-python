def binarysearch(L,key):
	try:
		mid = len(L)//2
		if key == L[mid]:
			print("Match Found")
		elif key > L[mid]:
			binarysearch(L[mid+1:],key)
		elif key < L[mid]:
			binarysearch(L[:mid],key)
		else:
			print("Match not found")
	except IOError:
		print("Match not found")
	except IndexError:
		print("Match nhi mila")
		
	
l= [2,3,4,5,6,7]
binarysearch(l,8)