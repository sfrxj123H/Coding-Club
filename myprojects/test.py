def polyDivision(a1, b1, c1, a2, b2, c2):
    if a2 != 0:
        #c
        a = 0
        b = 0
        c = a1/a2
        rb = b1 - (a1*b2) / a2
        rc = c1 - (a1*c2) / a2
    elif b2 != 0:
        #bx + c
        a = 0
        b = a1/b2
        c = (b1*b2-a1*c2)/(b2*b2)
        rb = 0
        rc = c1 - c2*c
    elif c2 != 0:
        a = a1/c2
        b = b1/c2
        c = c1/c2
        rb = 0
        rc = 0
    else:
        return 0
    return (a, b, c, rb, rc)

from quadFuncLibrary import QuadFuncLibrary
tool = QuadFuncLibrary()
a1, b1, c1 = 1, -3, 2
a2, b2, c2 = 0, 1, -1
print(tool.formatFunc(a1, b1, c1))
print(tool.formatFunc(a2, b2, c2))
a3, b3, c3, rb, rc = polyDivision(a1, b1, c1, a2, b2, c2)
print(f"Results: {tool.formatFunc(a3, b3, c3)} remainder {tool.formatFunc(0, rb, rc)}")