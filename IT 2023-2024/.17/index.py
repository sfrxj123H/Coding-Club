def typeStr(x):
    return str(type(x))[8:-2]


string = input("String?\n")
print(f'"{string}" is a {typeStr(string)}')
print(f"'{string}' is also a {typeStr(string)}")
int1, int2 = 5, int(input("Please input an integer: 5, ...\n"))
print(f"{int1} + {int2} = {int1 + int2}. They are {typeStr(int1)}")
float1, float2 = 4.6, float(input("Please input an integer: 4.6, ...\n"))
print(f"{float1} + {float2} = {float1 + float2}. They are {typeStr(float1)}")
boolean1, boolean2 = True, False
if boolean1:
    print(f"{boolean1} is to mark pass")
if not boolean2:
    print(f"{boolean2} is to mark fail")
print(f"They both type {typeStr(boolean1)}")
list_ = ["yesss", int1, float1, boolean1]
print(f"{list_} is a {typeStr(list_)}, they can include any type")
dict_ = {"string": "yesss", "integer": int1, "float": float1, "boolean": boolean1}
print(f"{dict_} is a {typeStr(dict_)}")
