def grep(pattern):
    print('start grep')
    while True:
        line = yield
        if pattern in line:
            print(line)

g = grep('python')
print(type(g))
next(g)
g.send('golang is better')
g.send('python is simple')
g.close()
