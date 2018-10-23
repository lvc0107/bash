#time complexity = 80%
def solution(N, A):

    counters = [0] * N
    max_counter = 0
    for i in A:
        if i <= N:
            counters[i - 1] += 1
            if counters[i - 1] > max_counter:
                max_counter = counters[i - 1]
        else:
            counters = [max_counter] * N

    return counters

#time complexity = 40%

def solution2(N, A):

    counters = [0] * N
    for i in A:
        if i <= N:
            counters[i - 1] += 1
        else:
            counters = [max(counters)] * N

    return counters



def solution3 (N, A):
    result = [0]*N    # The list to be returned
    max_counter = 0   # The used value in previous max_counter command
    current_max = 0   # The current maximum value of any counter
    for command in A:
        if 1 <= command <= N:
            # increase(X) command
            if max_counter > result[command-1]:
                # lazy write
                result[command-1] = max_counter
            result[command-1] += 1
            if current_max < result[command-1]:
                current_max = result[command-1]
        else:
            # max_counter command
            # just record the current maximum value for later write
            max_counter = current_max
    for index in range(0,N):
        if result[index] < max_counter:
            # This element has never been used/updated after previous
            #     max_counter command
            result[index] = max_counter
    return result





A = [3, 4, 4, 6, 1, 4, 4]
N = 5
x = solution(N, A)
print(x)

