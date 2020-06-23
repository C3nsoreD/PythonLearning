# Gabriel Richard Ugolole

# Solving the matrix chain problem using dynamic programming paradim

#define the Matix Chain
import sys

def MatrixChain(mat, i, j):
	#mthe algorithm doesnot compute for identity matrices.. i.e i==j
	if i == j:
		return 0
	min_computations = sys.maxsize
	
	for k in range(i, j):
		#Recursion call
		count = (MatrixChain(mat, i, k) + MatrixChain(mat, k+1, j)+ mat[i-1]*mat[k]*mat[j])
		print(count) #Weird behaviour 
	
	# Base Case 
	if count < min_computations:
		
		min_computations = count


	return min_computations

matrix_size = (20, 30, 45, 50)
print("Minimum multiplications are", MatrixChain(matrix_size, 1, len(matrix_size)-1))