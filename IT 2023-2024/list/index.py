a = range(0, 10, 2)
b = list(a)
c = ["nick", "daudau", "bachhhh", 123, 789]
print("a:", a, "=>", type(a), "length:", len(a), "=> this is a range")
print("b:", b, "=>", type(b), "length:", len(a), "=> range is also considered as a list")
print("c:", c, "=>", type(c), "length:", len(a), "=> this is a list")
c.append("yes")
print("append(obj) to add obj at the end")
c.insert(2, 1.234)
print("insert(index, obj) to add obj at index position")
c.remove(123)
print("remove(obj) to delete an obj value from the list")
c.pop(-2)
print("remove(index=-1) to delete value in the index position (default: last position)")
print("c:", c, "=> new", "length:", len(a))
print("pos 2 in a is:", a[2])
print("pos 2 in b is:", b[2])
print("pos 4 in c is:", c[4])
print("pos -1 in c is:", c[-1])
print("list addictive pos: [0, 1, 2, 3, 4, 5, ...]")
print("list subtractive pos: [..., -6, -5, -4, -3, -2, -1]")
c_printer = []
for i in range(len(c)):
    c_printer.append(i)
print("for results 1:", *c_printer)
c_printer = []
for i in range(len(c)):
    c_printer.append(c[i])
print("for results 2:", *c_printer)
c_printer = []
for i in c:
    c_printer.append(i)
print("for results 3:", *c_printer)
