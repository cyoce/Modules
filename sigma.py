def sigma(a=None,b=None,c=None,enum=False):
    mn = 1
    mx = 10
    fn = lambda x: x
    if type(a) == list:
        vals = a
        if hasattr(b,'__call__'): fn = b
    else:
        if hasattr(a,'__call__'):
            fn = a
        elif type(b) in (int,float):
            mn = a
            mx = b
            if hasattr(c,'__call__'): fn = c
        elif type(a) in (int,float):
            mx = a
            if hasattr(c,'__call__'): fn = b
        vals = list(range(mn,mx+1))
    vals = list(map(fn,vals))
    sm = 0
    out = []
    for i,x in enumerate(vals):
        sm += x
        out.append(sm)
    return out if enum else sm
