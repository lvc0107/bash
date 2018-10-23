
def solution(A, B):

    N = len(A)
    full_list = set(range(1, N + 1))
    if A == B:
        if set(A) == full_list:
            return N + 1
        else:
            return min(full_list - set(A))

    if set(A) == full_list:
        return N + 1

    missing_in_list_A = full_list - set(A) #3
    min_A = min(missing_in_list_A) #3
    missing_in_list_B = missing_in_list_A & set(B) #3
    for i in B:
        if i in missing_in_list_B:
            A[i] = B[i]
            missing_in_list_A = full_list - set(A)  # 4
            missing_in_list_B = missing_in_list_A & set(B) #
            if not missing_in_list_B:
                break


A = [1, 2, 4, 3]
B = [1, 3, 2, 3],
x = solution(A, B)
print(x)

A = [4, 2, 1, 6, 5]
B = [3, 2, 1, 7, 7]
x = solution(A, B)
print(x)

A = [2, 3]
B = [2, 3]
x = solution(A, B)
print(x)
