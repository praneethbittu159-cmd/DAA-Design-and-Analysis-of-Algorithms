# Insertion Sort
# Time Complexity:
# Best Case    : O(n)
# Average Case : O(n^2)
# Worst Case   : O(n^2)
#
# Space Complexity:
# O(1)
def insertion_sort(arr):
   n=len(arr)

   for i in range(1,n):
    key=arr[i]
    j=i-1

    while j>=0 and arr[j]>key:
        arr[j+1] = arr[j]
        j-= i
    arr[j+1] = key
arr= [12,3,8,9,2]

insertion_sort(arr)

print("sorted array : ",arr)
#Insertion Sort is a sorting algorithm that builds the sorted array one element at a time.
#Take one element and insert it into its correct position among the already-sorted elements.