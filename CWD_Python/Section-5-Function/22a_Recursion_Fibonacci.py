'''Fibonacci series
  
           index --> 0  1  2  3  4  5  6  7
           
Fibonacci series --> 0  1  1  2  3  5  8  13
'''
n = int(input("Enter the term for which you want the sum:"))

def fib(n):
    if(n==0 or n==1):  #Base case
        return n
    else:
        return fib(n-2)+ fib(n-1)  # Recursion Case
    
print(fib(n))