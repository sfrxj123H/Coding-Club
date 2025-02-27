def intIf(num):
    if num // 1 == num:
        return int(num)
    else:
        return num


print(
    "Các ứng dụng sử dụng Python:\n\n- Chrome\n- Opera\n- Microsoft Edge\n- Geometry Dash\n- Roblox\n- Word\n- Powerpoint\n- Excel\n- ChatGPT\n...")
print("\n\nPitago - Tam giác vuông")
r = input("Bấm để bắt đầu Pitago, e để thoát: ")
while r != "e":
    print("\n")
    x = float(input("Cạnh góc vuông 1: "))
    y = float(input("Cạnh góc vuông 2: "))
    print(f"Cạnh huyền: {intIf((x ** 2 + y ** 2) ** (1 / 2))}")
    r = input("Bấm để thử lại, e để thoát: ")
print("     *\n    ***\n   *****\n  *******\n *********\n***********\n    | |")
