def decimal(m):
    s=str(m)
    s1,j=0,0
    for i in s[-1::-1]:
        s1+=int(i)*(2**j)
        j+=1
    return s1
a=input("Enter the binary number separated by comma")
l=a.split(",")
print(l)
l1=[]
for i in l:
    l.append(decimal(i))
for i in range(len(l1)):
    if l1[i]%5==0:
        print(l1[i])    
        
