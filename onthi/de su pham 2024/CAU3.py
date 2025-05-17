import time, random
# n = [int(i) for i in input().split(" ")]
# a = [int(i) for i in input().split(" ")]
limit = 15000
n = [limit, 15 * limit]
a = [random.randint(1, 30) for _ in range(limit)]
print(a)
print("Random completed")
x = time.time()
m = n[1]
n = n[0]
if min(a) >= m:
    print(1)
elif sum(a) < m:
    print(-1)
else:
    for k in range(2, n+1):
        if all(sum(a[i:k+i]) >= m for i in range(0, n-k+1)):
            print(k)
            break
y = float(time.time() - x)
print(f"Thời gian: {y:.4f} giây")