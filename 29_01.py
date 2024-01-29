def f(x):
    S = 0
    while x != 0:
        S += x % 10
        x // 10
        return S


def ff(x):
    S = 0
    for i in x:
        S += int(i)


def fff(x):
    return sum(map(int, x))
