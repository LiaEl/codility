'''
Task:
 Write a function:
 def solution(A)
 that, given an array A of N integers, returns the smallest positive integer
 (greater than 0) that does not occur in A.
 For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
 Given A = [1, 2, 3], the function should return 4.
 Given A = [−1, −3], the function should return 1.
'''

def solution(A):
    A = [i for i in A if i > 0]
    if not A:
        return 1
    mint = min(A)
    if mint != 1:
        return 1
    while mint in A:
        mint += 1
    else:
        return mint

print(solution([-1, -2, -3]))
