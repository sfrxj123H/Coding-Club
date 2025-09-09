import random, time
n, p = list(map(int, input().split(" ")))
# a = list(map(int, input().split(" ")))
a = [random.randint(1, int(p * 1.5)) for _ in range(n)]
print("Random array generated")
x = time.time()
a.sort()
ans = 0
for i in range(n):
    partner = a[::-1]
    partner.append(p - a[i])
    ans += sorted(partner).index(p - a[i], )
print(ans)
y = float(time.time() - x)
print(f"Thời gian: {(y):.4f} giây")