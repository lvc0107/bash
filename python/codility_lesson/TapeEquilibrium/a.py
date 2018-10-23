

def solution(A):
    s = sum(A)
    for i in range(len(A)):
        B = A[:i]
        C = A[i:]
        s = min(s, abs(sum(B) - sum(C)))

    return s



A = [3, 1, 2, 4, 3]
x = solution(A)
print(x)

