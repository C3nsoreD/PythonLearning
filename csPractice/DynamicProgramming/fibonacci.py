# Fibonacci using recursion

def fib(n):
    #Base case 
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Function to calculate nth Fibonacci number 
lookup = [None]*(101) 
def fib_memo(n, lookup): 
    # Base case 
    if n == 0 or n == 1 : 
        lookup[n] = n 
    # If the value is not calculated previously then calculate it 
    if lookup[n] is None: 
        lookup[n] = fib_memo(n-1 , lookup)  + fib_memo(n-2 , lookup)  
    # return the value corresponding to that value of n 
    return lookup[n] 

# Python program Tabulated (bottom up) version 
def fib_bottom_up(n): 
    # array declaration 
    f = [0]*(n+1) 
  
    f[1] = 1
    # calculating the fibonacci and storing the values 
    for i in range(2 , n+1): 
        f[i] = f[i-1] + f[i-2] 
    return f[n] 

if __name__  == "__main__":
    lookup = [None]*(10000) 
    print(fib_memo(1000, lookup))