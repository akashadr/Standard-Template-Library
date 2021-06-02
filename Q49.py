def findAllTriplets(A):
 
    if len(A) < 3:
        return
 
    for j in range(1, len(A) - 1):
 
        i = j - 1
        k = j + 1
 
        while i >= 0 and k < len(A):
 
            if A[i] + A[k] == 2 * A[j]:
 
                print((A[i], A[j], A[k]))
                
                k = k + 1
                i = i - 1
 
            elif A[i] + A[k] < 2 * A[j]:
                k = k + 1
            else:
                i = i - 1
 
 
if __name__ == '__main__':
 
    A = [5,8,9,11,12,15]
    findAllTriplets(A)