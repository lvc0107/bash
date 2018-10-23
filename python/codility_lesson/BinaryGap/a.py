
def solution(N):

    s = str(bin(N)).strip("0b")
    
    sl = len(s)
    bg = 0
    temp = 0
    for i in range(sl):
        if s[i] == "0":
            bg += 1
        if s[i] == "1":
            if temp < bg:
                temp = bg
            bg = 0
    return temp

