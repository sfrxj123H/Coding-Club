# print([ord(a) for a in "hello"][3])

# a = 2
# def func(b):
#     b=a*b
#     return lambda: a+b+c
# print(func(4)(3))

# a = {1: 2, 3: 4}
# for k, v in a.items():
#     print(k,v)

class C:
    a = 5
    def __init__(self):
        self.c = None

    def b(self, c = a):
        self.c = c
        return self.c

print(C().b().c)