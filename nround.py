def nround(x):
    x = float(x)
    if x % 1 >= 0.5:
        return int(x // 1 + 1)
    elif x % 1 < 0.5:
        return int(x // 1)
