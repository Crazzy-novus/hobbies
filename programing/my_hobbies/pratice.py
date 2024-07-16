n=eval(input("enter the vale of n:"))
prime=[]
for i in range(1,n+1):
    if(i==1):
        prime.append(i)
        #continue
    elif(i==2):
        prime.append(i)
        #continue
    elif(i>2):
        for j in range(2,i):
            a=i%j
            if(a==0):
                break
        if(a!=0):
            prime.append(i)
print("the first n prime number is ="+str(prime))