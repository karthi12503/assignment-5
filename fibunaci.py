arr = []
inc1=0
inc2=1
pos=0
n = int(input("Enter the length of an array:"))
for i in range(0,n):
     pos=i;
     if(pos==0):
        x=inc1
        arr.append(x)
     elif(pos==1):
        x=inc2
        arr.append(x)
     else:
        x=inc1+inc2
        arr.append(x)
        inc1=inc2
        inc2=x
print("Your array is:",arr)