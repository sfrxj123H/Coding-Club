b = 1
a = 5
i = int(input("StartPos (end is 5): "))
check = a - i
while check:
    x = input(f"For the {b} time, do you wanna stop, type sth to stop and enter to skip: ")
    if x:
        check = False
    else:
        check = a - i
        i += 1
        b += 1
        print(f"You have {check} times left")
print(f"You stopped the program in the {b} time!")