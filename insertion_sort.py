#EGE ALP TÜRKYENER
def insertion_sort(A): #creating function for insertion sort.



    for j in range(1, len(A)): #for the numbers from 1 to len(A)

        key = A[j] #save A[j] element to a temporary constant.


        i = j - 1

        # move the elements of array A if
        # it is greater than key.

        while i >= 0 and key < A[i]:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key

