hr1,mts1=input().split()
hr1,mts1=int(hr1),int(mts1)
hr2,mts2=input().split()
hr2,mts2=int(hr2),int(mts2)
v1=(hr1*60)+mts1
v2= (hr2*60)+mts2
absvalue=abs(v1-v2)
mts = absvalue  % 60
hrs = (absvalue - mts) / 60
print (int(hrs),int(mts))
