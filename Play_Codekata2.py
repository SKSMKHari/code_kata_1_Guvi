no=int(input("Enter the number:"))
strt=1
ind=1
while no>0:
    strt=strt*ind
    ind=ind+1
    no=no-1
print("Factorial:",strt)
