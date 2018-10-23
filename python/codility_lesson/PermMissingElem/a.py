def solution(A):
 N = len(A)
 x = sum(A)
 return sum(range(1, N + 2)) - x

A = [5, 2, 1, 3]
x = solution(A)
print(x)

