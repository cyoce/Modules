import turtle
def plot(a=None,b=None,c=None,scale=10):
    f = lambda x: x ** 2
    _min = -20
    _max = 20
    if hasattr(a,'__call__')   or type(a) == list:
        f = a
    elif hasattr(b,'__call__') or type(b) == list:
        f = b
        _max = a
    elif hasattr(c,'__call__') or type(c) == list:
        f = c
        _max = b
        _min = a
    if type(f) == list:
        _min = 0
        ls = f
        f = lambda i: ls[max(i,0)]
        _max = len(ls)-1
    pen = turtle.Turtle()
    pen.penup()
    pen.goto(_min*scale,f(_min))
    pen.pendown()
    for x in range(_min,_max+1):
        pen.goto(x*scale,f(x))
    turtle.exitonclick()
