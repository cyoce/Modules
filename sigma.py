def sigma(a=None,b=None,c=None):
    if type(a) == list:
        vals = a
        function = (lambda x: x) if b == None else b
    elif type(a) == int or type(a) == float:
         vals = range(a,b+1)
         function = (lambda x: x) if c == None else c
    out = 0
    for i in vals:
        out += function(i)
    return out
