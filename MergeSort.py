def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)

        i=j=k=0

        while i<len(left) and j<len(right):
            if left[i]< right[i]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[i]
                j+=1
            while i<len(left):
                arr[k]=left[i]
                i+=1
                k+=1
            while j<len(right):
                arr[k]=right[j]
                j+=1
                k+=1
arr=[18,27,13,19,8,3]
merge_sort(arr)
print("sorted array : ",arr)   
#Merge Sort is a divide-and-conquer sorting algorithm.
#It divides the array into smaller parts, sorts those parts, and then merges them back together.
# Merge Sort
# Time Complexity:
# Best Case    : O(n log n)
# Average Case : O(n log n)
# Worst Case   : O(n log n)
#
# Space Complexity:
# O(n)                     