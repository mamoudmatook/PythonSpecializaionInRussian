def chain(x_iterable, y_iterable):
    yield from x_iterable
    yield from y_iterable

a = [1, 2, 3]
b = [4, 5, 6]


g = chain(a, b)
print(type(g))

for x in g:
    print(x)