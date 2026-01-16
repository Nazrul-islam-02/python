def sum(a,b):
    return (a/b)


def outer(func):
    def inner(a,b):
        if a<b :
            a,b = b,a
        return func(a,b)
    return inner



result = outer(sum)

print(result(15,10))