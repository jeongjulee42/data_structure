def insertionSort(A):
    for i in range(1, len(A)):
        loc = i - 1
        newItem = A[i]
        while loc >= 0 and newItem < A[loc]:
            A[loc+1] = A[loc]
            loc -= 1
        A[loc+1] = newItem
        
#Test code 
list_A = [1,50,3,24,78,33]
insertionSort(list_A)
print(list_A)