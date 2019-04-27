def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(100))
a=fact(1)
print(a)


fact(5)
5 * fact(4)
5 * (4 * fact(3))
5 * (4 * (3 * fact(2)))
5 * (4 * (3 * (2 * fact(1))))
5 * (4 * (3 * (2 * 1)))
5 * (4 * (3 * 2))
5 * (4 * 6)
5 * 24


def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


if n == 1:
    print(a, '-->', c)
else:
    move(n-1, a, c, b)
    print(a, '-->', c)
    move(n-1, b, a, c)