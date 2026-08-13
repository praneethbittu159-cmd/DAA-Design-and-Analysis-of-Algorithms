#sorting Algorithm
#Bubble sort
#time complexity
#Best case:o(n)
#Average case:o(n^2)
#worst case:o(n^2)
#Space complexity:o(1)
def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
      for j in range(0, n-i-1):
        if arr[j]>arr[j+1]:
          arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[64,34,25,12,22,11,90]

BubbleSort(arr)

print("sorted Array:")
print(arr)
#Summary
#Bubble Sort is a sorting algorithm 
#that repeatedly compares two adjacent elements and swaps them if they are in the wrong order.