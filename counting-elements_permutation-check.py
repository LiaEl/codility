'''
Task:
 A non-empty array A consisting of N integers is given.
 A permutation is a sequence containing each element from 1 to N once, and only once.
 For example, array A such that:
     A[0] = 4
     A[1] = 1
     A[2] = 3
     A[3] = 2
 is a permutation, but array A such that:
     A[0] = 4
     A[1] = 1
     A[2] = 3
 is not a permutation, because value 2 is missing.
 The goal is to check whether array A is a permutation.
 Write a function:
 def solution(A)
 that, given an array A, returns 1 if array A is a permutation and 0 if it is not.
 For example, given array A such that:
     A[0] = 4
     A[1] = 1
     A[2] = 3
     A[3] = 2
 the function should return 1.
 Given array A such that:
     A[0] = 4
     A[1] = 1
     A[2] = 3
 the function should return 0.
'''
def solution(A):
    if min(A) != 1:
        return 0
    if len(A) not in A:
        return 0
    mint = 1
    while mint in A:
        mint += 1
    if mint - 1 != len(A):
        return 0
    else:
        return 1

print(solution([4, 3, 2, 1]))
print(solution([4, 3, 1]))
