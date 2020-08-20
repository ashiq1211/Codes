n=int(input("Enter a number: "))
sum=0
num=n
digits=len(str(n))
while n>0:
    rem=n%10
    sum=sum+pow(rem,digits)
    n=n//10

if sum==num:
    print(num,"is Armstrong")
else:
    print(num,"is not Armstrong")
