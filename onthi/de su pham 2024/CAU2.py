import time
n = int(input())
xau = input()
x = float(time.time())
out = 0
for i in range(1, n+1):
    if not any(ch in xau for ch in str(i)):
        out += 1
y = float(float(time.time()) - x)
print(y)
print(out)