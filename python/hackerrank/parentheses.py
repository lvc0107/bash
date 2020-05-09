
def is_balanced(a):
    if not a:
        return False
    p = {"[": "]", "{": "}", "(": ")"}
    stack = []
    for idx, val in enumerate(a):
        if val in p.keys():
            stack.append(val)
        elif stack and p[stack[-1]] == val:
            stack.pop()

    return stack == []


a = "(a[0]+b[2c[6]]){24 + 53}"
print(a, is_balanced(a))
a = "f(e(d))"
print(a, is_balanced(a))
a = "[()]{}([])"
print(a, is_balanced(a))
a = "((b)"
print(a, is_balanced(a))
a = "(c]"
print(a, is_balanced(a))
a = "{(a[])"
print(a, is_balanced(a))
a = "([)]"
print(a, is_balanced(a))
a = ")("
print(a, is_balanced(a))
a = ""
print(a, is_balanced(a))



# solucion que solamente contempla "()"
def matched(str):
    count = 0
    for i in str:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0
