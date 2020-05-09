def numMasPopular(a):
    result = []
    b = list(set(a))
    for i in range(1, len(b) + 1):
        result.append([(i), a.count(i)])

    list_max = []
    max_n = 0
    for num in result:
        if num[1] > max_n:
            max_n = num[1]
            list_max = []
        elif num[1] == max_n:
            max_n = num[1]
        list_max.append(num[0])

    if len(list_max) == 1:
        return list_max[0]
    else:
        return min(list_max)


print(numMasPopular([1, 1, 2, 2, 3]))
