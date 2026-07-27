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

#Time complexity:
#Best case:o(n^2)
#Average case:o(n^2)
#Worst case:o(n^2)
#Space complexityo(1)