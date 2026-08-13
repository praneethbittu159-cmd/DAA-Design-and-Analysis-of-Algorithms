def iterative_factorial(n):
    fact = 1

    for i in range(1,n+1):
        fact*=i

    return fact    
n=int(input("number : ")) 
result=iterative_factorial(n)
print("fact = ",result)
#summary
#Factorial iteration is a simple way 
#of finding the factorial of a number using a loop. 
#We start with fact = 1 and then multiply it by each number from 1 up to the given number.