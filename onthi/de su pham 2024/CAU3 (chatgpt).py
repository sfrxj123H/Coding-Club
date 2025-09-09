import time, random, pyperclip

limit = 1000000
n, m = limit, 15 * limit
a = [random.randint(1, 30) for _ in range(n)]
pyperclip.copy(str(a))
print("Random completed")

x = time.time()

if min(a) >= m:
    print(1)
elif sum(a) < m:
    print(-1)
else:
    # Prefix sum
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + a[i]

    # Hàm tính tổng đoạn con a[l:r]
    def range_sum(l, r):
        return prefix_sum[r] - prefix_sum[l]

    # Tìm k nhỏ nhất sao cho mọi đoạn con độ dài k có tổng >= m
    for k in range(2, n+1):
        for i in range(0, n - k + 1):
            if range_sum(i, i + k) < m:
                break
        else:
            print(k)
            break

y = time.time() - x
print(f"Thời gian: {y:.4f} giây")