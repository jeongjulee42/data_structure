def selectionSort(A):
    for last in range(len(A)-1, 0, -1):
        k = theLargest(A, last)
        A[k], A[last] = A[last], A[k]
        
def theLargest(A, last):
    largest = 0
    for i in range(last+1):
        if A[i] > A[largest]:
            largest = i
    return largest


#Test code 
list_A = [1,50,3,24,78,33]
selectionSort(list_A)
print(list_A)