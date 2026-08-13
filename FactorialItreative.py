def iterative_factorial(n):
    fact = 1

    for i in range(1,n+1):
        fact*=i

    return fact    
n=int(input("number : ")) 
result=iterative_factorial(n)
print("fact = ",result)