# Python program for implementation of MergeSort 
## Time Complexity O(nlog(n))
## Space Complexity O(n)
def mergeSort(arr):
  
  #write your code here
  if len(arr) == 1:
    return arr
  
  mid = len(arr) // 2
  left, right = mergeSort(arr[:mid]), mergeSort(arr[mid:])
  i,j, index = 0,0, 0
  #print(right, " right")
  #print(left, " left")

  while i < len(left) and j < len(right):

    if left[i] < right[j]:
        arr[index] = left[i]
        i += 1
    else:
        arr[index] = right[j]
        j += 1
    index += 1

  while i != len(left):
    arr[index] = left[i]
    index += 1
    i+= 1
  while j != len(right):
    arr[index] = right[j]
    index += 1
    j += 1

  return arr


  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    for i in arr:
        print(i, end = " ")
    print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
