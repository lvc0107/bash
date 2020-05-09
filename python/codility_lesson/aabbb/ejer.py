# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A, B):
    if A == B:
        return 'ab' * A

    if A > B:
        x = 'a'
        y = 'b'
        big = A
        small = B
    else:
        x = 'b'
        y = 'a'
        big = B
        small = A

    res = ''
    while big != small:
        big -= 2
        small -= 1
        res += 2 * x + y
    if big == small:
        while big > 0:  # or small > 0
            big -= 1
            small -= 1
            res += x + y
    return res

    # incomplete


if __name__ == "__main__":
    A = 2
    B = 5
    solution(A, B)
