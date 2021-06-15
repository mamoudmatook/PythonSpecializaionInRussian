def grep(pattern):
    print("start grep")
    while True:
        line = yield
        if pattern in line:
            print(line)


def grep_python_coroutine():
    g = grep("python")
    yield from g

g = grep_python_coroutine()
print(type(g))
next(g)
g.send('python wow!')
