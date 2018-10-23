
# Solution with XOR operator.
def solution(A):
    result = 0
    for number in A:
        result ^= number;

    return result


A = [7, 9, 3, 9, 3, 9, 3]
x = solution(A)
print(x)


# my solution
def solution(A):
    for x in A:
        if A.count(x) == 1:
            return x


A = [7, 9, 3, 9, 3, 9, 3]
B = [9, 3, 9, 3, 9, 7, 9]

x = solution(A)
print(x)

x = solution(B)
print(x)
