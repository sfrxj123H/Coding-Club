import time

n = 100000
xau = "01256789"

x = time.time()

broken = set(xau)
out = 0
for i in range(1, n + 1):
    if not any(ch in broken for ch in str(i)):
        out += 1

y = float(time.time() - x)
print(f"Thời gian: {y:.4f} giây")
print(out)