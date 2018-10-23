"""
def solution(T):
    x = len(T)/4
    seasons = [T[i:i + x] for i in range(0, len(T), x)]
    x = [max(s) - min(s) for s in seasons]

    h_t = max(x)
    if h_t == x[0]:
        return "WINTER"
    if h_t == x[1]:
        return "SPRING"
    if h_t == x[2]:
        return "SUMMER"
    if h_t == x[3]:
        return "AUTUMN"


A = [3, -14, -5, -7, 8, 42, 8, 3]
s = solution(A)
print s


A = [2, -3, 3,  1, 10, 8, 2, 5, 13, -5, -3, -18]
s = solution(A)
print s

[2, 1, 1, 10, 2, 13, 3, -18]
s = solution(A)
print s
"""


def solution(A, B):

    if A > B:
        if A - B <= B + 1:
            if A % 3 == 0:
                a = A // 2
                if B % 3 == 0:
                    b = B // 2
                    return ('aab' * a)
                else:
                    pass
    elif B > A:
        if B - A <= A + 1:
            if B % 3 == 0:
                b = B // 2
                return ('bba' * b) + 'b'
            else:
                pass
    else:
        return 'ab' * A


A = 6
B = 6
s = solution(A, B)
print s


A = 9
B = 6
s = solution(A, B)
print s


ple test:    (5, 3)
Output (stderr):
Invalid result type, string expected, <class 'NoneType'> found.
RUNTIME ERROR  (tested program terminated with exit code 1)

Example test:    (3, 3)
OK

Example test:    (1, 4)
Output (stderr):
Invalid result type, string expected, <class 'NoneType'> found.
RUNTIME ERROR  (tested program terminated with exit code 1)

Detected some errors.