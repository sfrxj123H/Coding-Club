class A:
    x = 3

def func(a):
    print(a.x)

a = A()
a.x = 2
A.func = func
a.func()