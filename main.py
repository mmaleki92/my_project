def fun():
    return 2


def fun4(a, b):
    if b == 0:
        pass
    return a/b

a, b = int(input()), int(input())
c = fun4(a, b)
print(c)


