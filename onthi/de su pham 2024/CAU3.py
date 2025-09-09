import time, random, pyperclip

#Sample input:
# n, m = 6, 10
# a = [3, 5, 6, 4, 5, 1]

#Normal input:
# n, m = [int(i) for i in input().split(" ")]
# a = [int(i) for i in input().split(" ")]

#Random input:
limit = 1000000
n, m = limit, 15 * limit
a = [random.randint(1, 30) for _ in range(n)]
pyperclip.copy(str(a))
print("Random input generated")

x = time.time()
if min(a) >= m:
    print(1)
elif sum(a) < m:
    print(-1)
else:
    prefix_sum = [0] * (n + 1)
    for q in range(n):
        prefix_sum[q + 1] = prefix_sum[q] + a[q]

    z = float(time.time() - x)
    print(f"Thời gian: {z:.4f} giây")

    x = time.time()
    def range_sum(ind, length):
        return prefix_sum[length + ind] - prefix_sum[ind]
        
    for k in range(2, n + 1):
        for i in range(0, n - k + 1):
            if range_sum(i, k) < m:
                break
        else:
            print(k)
            break
    
y = float(time.time() - x)
print(f"Thời gian: {(y):.4f} giây")