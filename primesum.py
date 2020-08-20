n=int(input("Enter a number: "))
primes=[]
count=0

for i in range (3,n+1):
     flag=0
     for j in range (2,i):
         if(i%j==0):
             flag=1

     if(flag==0):
        primes.append(i)
print(primes)
for prime in primes:
    sum=2
    for i in range (3,prime):
        f=0
        for j in range (2,i):
            if(i%j==0):
                f=1
        if(f==0):
            sum=sum+i
        if(sum==prime):
         count=count+1
         print(sum)
         break
print(count)
