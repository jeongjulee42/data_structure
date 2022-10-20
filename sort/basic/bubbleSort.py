def bubbleSort(A):
    for numElements in range(len(A), 0, -1):
        for i in range(numElements-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                
                
#Test code 
list_A = [1,50,3,24,78,33]
bubbleSort(list_A)
print(list_A)