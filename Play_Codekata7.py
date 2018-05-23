ipv=input("Enter the String:")
ipv=list(ipv)
for i in range(0,len(ipv)-1,2):
    ipv[i],ipv[i+1]=ipv[i+1],ipv[i]
print ("".join(ipv))
