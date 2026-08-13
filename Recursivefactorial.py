def recursive_factorial(n):
    if n==0 or n==1:
        return 1
    return n * recursive_factorial(n-1)

n=int(input("Number : ")) 
result=recursive_factorial(n)
print("fact : ",result)  
# Summary
#recursion is the process of function calling itself.Recursive factorial calculates the factorial of a number by having a function call itself with a smaller value. The function keeps reducing n by 1 until it reaches the base case, where n is 0 or 1 and the function returns 1.
# Time Complexity:
# Best Case    : O(n)
# Average Case : O(n)
# Worst Case   : O(n)
#
# Space Complexity:
# O(n)     