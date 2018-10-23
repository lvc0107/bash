


#O(n)
def solution(X, Y, D):
    jumps = 0
    while X < Y:
        X += D
        jumps += 1
    return jumps


#O(1)
def solution2(X, Y, D):

    distance = Y - X
    if distance % D == 0:
        return distance//D
    else:
        return distance//D + 1


X = 10
Y = 85
D = 30
s = solution(X, Y, D)
print(s)
