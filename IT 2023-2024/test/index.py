a = []
for i in range(5):
    x = input(f"Append to position {i + 1}: ")
    try:
        a.append(eval(x))
    except:
        a.append(x)
print(a)
