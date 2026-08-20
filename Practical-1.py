#Bubble sort
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

#Selection sort
#SelectionSort
def SelectionSort(arr):
  n=len(arr)
  for i in range(n-1):
    min_index=1

    for j in range(i+1,n):
      if arr[j]<arr[min_index]:
        min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]


arr=[64,34,25,12,22,11,90]
SelectionSort(arr)
print("sorted Array:")
print(arr)

#Insertion Sort
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

#Merge Sort
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

#Quick Sort
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


