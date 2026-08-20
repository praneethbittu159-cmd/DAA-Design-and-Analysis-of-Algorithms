#Iterative Factorial
def iterative_factorial(n):
    fact = 1

    for i in range(1,n+1):
        fact*=i

    return fact    
n=int(input("number : ")) 
result=iterative_factorial(n)
print("fact = ",result)

#Recursive Factorial
def recursive_factorial(n):
    if n==0 or n==1:
        return 1
    return n * recursive_factorial(n-1)

n=int(input("Number : ")) 
result=recursive_factorial(n)
print("fact : ",result)  
