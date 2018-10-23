def solution(A, k):
    k -= 1
    return A[k:] + A[:k]


A = [3, 8, 9, 7, 6]
x = solution(A, 3)
print(x)

