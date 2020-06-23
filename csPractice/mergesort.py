#Merge Sort implementation

def mergeSort(arr):

	if len(arr)>1:
		print("test print", arr)
		mid = len(arr)//2
		left = arr[:mid]
		right = arr[mid:]

		mergeSort(left)
		print("working on the inner block")
		mergeSort(right)

		i = j = k = 0
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				arr[k] = left[i]		
				i+=1
			else:
				arr[k]=right[j]
				j+=1
			k+=1

		while i < len(left):
			arr[k] = left[i]
			i+=1
			k+=1

		while j<len(right):
			arr[k] = right[j]
			j+=1
			k+=1
	
		print(arr)
	return arr

mergeSort([12,34,19,17,94])