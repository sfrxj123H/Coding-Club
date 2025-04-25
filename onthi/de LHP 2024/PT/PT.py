def inout(tenfile, string=""):
    if string: open(tenfile, "w").write(string)
    else: return [int(i) for i in open(tenfile, "r").read().split(" ")]

array_inp = inout("PT.INP")
if array_inp[0] != 0:
    # NDN
    kq = "NDN"
elif array_inp[1] == 0:
    # VSN
    kq = "VSN"
else:
    # VN
    kq  = "VN"
inout("PT.OUT", kq)