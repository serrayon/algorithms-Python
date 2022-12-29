def find3Numbers(A, arr_size, sum):
    for i in range(0, arr_size-1):
        # Find pair in subarray A[i + 1..n-1]
        # with sum equal to sum - A[i]
        s = set()
        curr_sum = sum - A[i]
        for j in range(i + 1, arr_size):
            if (curr_sum - A[j]) in s:
                print("Triplet is", A[i],
                        ", ", A[j], ", ", curr_sum-A[j])
                return True
            s.add(A[j])
     
    return False
 
# Driver program to test above function
A = [1, 4, 45, 6, 10, 8]
sum = 22
arr_size = len(A)
find3Numbers(A, arr_size, sum)
