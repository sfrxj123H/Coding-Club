import time
n = int(input())
x = time.time()
def gcd(m, n):
    if n % m == 0:
        return m
    for i in range(m // 2, 0, -1):
        if m % i == 0 and n % i == 0:
            return i
cd = []
ms = []
for m in range(n-2, 0, -1):
    cd.append(gcd(m, n) + m)
    ms.append(m)
print(float(time.time() - x) * 1024**2)
print(ms[cd.index(max(cd))])