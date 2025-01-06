def quickSort(arr,low, high):

  if low < high:

    pi = partition(arr, low, high)

    quickSort(arr, low, pi - 1)
    quickSort(arr, pi + 1, high)
  
  return arr


def partition(arr, low, high):

  #define i
  i = low - 1
  
  #define pivot
  pivot = arr[high - 1]
  print(pivot)
  #define tempory value
  temp = 0

  for j in range(low,high):

    if(arr[j] <= pivot):
      i+= 1
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
  
    j += 1

  return i 


arr = [8,2,4,7,1,3,9,6,5]
quickSort(arr, 0, len(arr))

#https://www.youtube.com/watch?v=Vtckgz38QHs
