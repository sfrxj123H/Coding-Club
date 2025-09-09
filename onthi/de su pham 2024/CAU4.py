from itertools import combinations

# Tạo danh sách các số có chữ số tăng dần không lặp, từ 1 đến 9
valid_numbers = []
digits = '123456789'
for l in range(1, 10):
    for comb in combinations(digits, l):
        valid_numbers.append(int(''.join(comb)))
valid_numbers.sort()

# Hàm xử lý từng test case
def solve(a):
    # Duyệt ngược để tìm số lớn nhất ≤ a
    for num in reversed(valid_numbers):
        if num <= a:
            return num

# Nhập và xử lý
T = int(input())
for _ in range(T):
    a = int(input())
    print(solve(a))
