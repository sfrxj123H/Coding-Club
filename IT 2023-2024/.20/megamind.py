print("Mega não to!: Điểm thi")
z = 0
for i in range(12):
    print("\nLớp", i + 1)
    x = input("Megamind có nghiện không? (Để trống: Không): ")
    if x:
        y = input("Megamind có gian lận không?: ")
        if not y:
            score = float(input("Nhập số điểm: "))
            y = "a" if score >= 5 else ""
    if not x or y:
        print("Vượt")
        z += 1
    else:
        print("Trượt")
print(f"\nMega não to qua {z}/6 lớp cần thiết!")
if z >= 6:
    print("\nMega não to lương 100 củ.")
else:
    print("\nMega não to lương 500k.")