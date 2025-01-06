def mergeSort(arr):

  
  if len(arr) <= 1:
    return arr

  #find middle part of array
  mid = len(arr) // 2

  #split array into left and right
  leftArray = arr[:mid]
  rightArray = arr[mid:]

  #keep splitting arrays
  sortedLeft = mergeSort(leftArray)
  sortedRight = mergeSort(rightArray)
  
  return merge(sortedLeft, sortedRight)




def merge(left, right):
  result = []
  i = j = 0


  while i < len(left) and j < len(right):
      if left[i] < right[j]:
          result.append(left[i])
          i += 1
      else:
          result.append(right[j])
          j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

arr = [8,2,5,3,4,7,6,1]

print(mergeSort(arr))

#https://www.youtube.com/watch?v=3j0SWDX4AtU&t=29s
