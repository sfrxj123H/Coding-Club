xString = input('Enter multiple values (separate with ","): ')
try:
    eval(xString)
except ValueError:
    pass
xList = list(eval(xString + ", 1"))[:-1]
print("Your list:", xList)
print("Length of your list:", len(xList))