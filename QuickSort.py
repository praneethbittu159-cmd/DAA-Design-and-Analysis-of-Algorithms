def partition(arr, low, high):
    pivot = arr[high]

    i = low-1
    for j in range(low, high):

        if arr[j] < pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1

def quickSort(arr, low, high):
    if low<high:
        pi=partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)          

arr = [13,10,8,2,6]
quickSort(arr, 0, len(arr) - 1)
print(arr)
#Quick Sort is another divide-and-conquer sorting algorithm.
#and chooses an element as pivot and sorts
#Pivot:The element chosen around which the array is partitioned.
#Partition:The process of placing smaller elements on one side of the pivot and larger elements on the other.
#Time complexity
#Best: O(n log n)
#Average: O(n log n)
#Worst: O(n²)

