def calculate(data, findall):
    matches = findall(r"([abc])([+-])?=([abc])?([+-]?\d+)?")
    for v1, s, v2, n in matches:
        rhs = data.get(v2, 0) + int(n or 0)
        if s == '+':
            data[v1] += rhs
        elif s == '-':
            data[v1] -= rhs
        else:
            data[v1] = rhs
    return data