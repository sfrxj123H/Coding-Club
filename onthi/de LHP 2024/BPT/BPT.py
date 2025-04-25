def inout(tenfile, string=""):
    if string: open(tenfile + ".OUT", "w+").write(string)
    else: return [int(i) for i in open(tenfile + ".INP", "r").read().split(" ")]

n = inout("BPT")[0]
print(n)
out = 0

def f(x):
    return sum([int(i) for i in str(x)])

for x in range(1, n+1):
    if f(x+1) < f(x):
        out += 1
    print(x, " ", out)

inout("BPT", str(out))