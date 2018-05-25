t = int(input())
hr = t //60
t %= 60
mts = t // 1
print("%d %d" % (hr,mts))
