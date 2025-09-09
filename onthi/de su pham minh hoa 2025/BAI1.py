import math, time
n = int(input())
x = time.time()
scp = [0] * (n + 1)
for i in range(1, n + 1):
    scp[i] = i * i
print("this one done")
yes = 0
for i in range(1, n + 1):
    print("testing i =", i)
    for j in range(1, n + 1):
        if i * j in scp:
            yes += 1
print(yes)
y = float(time.time() - x)
print(f"Thời gian: {(y):.4f} giây")