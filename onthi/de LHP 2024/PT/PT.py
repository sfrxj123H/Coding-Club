def inout(tenfile, string="", allowletters=False):
    if string:
        open(tenfile + ".OUT", "w+").write(string)
        exit()
    elif allowletters or not open(tenfile + ".INP", "r").read().isnumeric():
        inout(tenfile, "Input includes alpha error!")
    else: return [int(i) for i in open(tenfile + ".INP", "r").read().split(" ")]

array_inp = inout("PT")
if array_inp[0] != 0:
    # NDN
    kq = "NDN"
elif array_inp[1] == 0:
    # VSN
    kq = "VSN"
else:
    # VN
    kq  = "VN"
inout("PT", kq)