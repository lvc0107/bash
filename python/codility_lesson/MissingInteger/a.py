# this solution is  for max missing integer
def solution2(A):

    N = max(A)
    if N <= 0:
        return 1

    max_i = 0
    for i in A:
        if i > max_i and i < N:
            max_i = i

    if max_i == N - 1:
        return N + 1
    else:
        return max_i + 1

# solution for min missing integer
# 77 %
def solution(A):

    N = max(A)
    if N <= 0:
        return 1
    full_list = list(range(1, N + 1))
    if full_list == A:
        return N + 1

    return min(set(full_list) - set(A))

# solution for min missing integer
# 88 %
def solution(A):
    N = max(A)
    if N <= 0:
        return 1
    full_list = set(range(1, N + 1))
    A = set(A)
    if full_list == A:
        return N + 1

    return min(full_list - A)

A = [1, 3, 6, 4, 1, 2]
s = solution(A)
print(s)

A = [1, 2, 3]
s = solution(A)
print(s)

A = [-1, -3]
s = solution(A)
print(s)