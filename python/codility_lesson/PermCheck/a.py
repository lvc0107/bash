
def solution(A):

    N = set(A)
    M = set(range(1, len(A) + 1))
    return N == M


A = [1, 2, 3, 4]
B = [1, 3, 4]

x = solution(A)
print(x)

x = solution(B)
print(x)

