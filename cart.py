def cross(a,b):
    out = set()
    for x in a:
        for y in b:
            out.add((x,y))
    return out

def sub(s,f):
    out = set()
    for t in s:
        x = t[0]
        y = t[1]
        if f(x,y): out.add((x,y))
    return out

def dom(s):
    out = set()
    for t in s:
        out.add(t[0])
    return out

def ran(s):
    out = set()
    for t in s:
        out.add(t[1])
    return out
