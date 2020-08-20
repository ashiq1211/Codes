def fib(num):
  a=0
  b=1
  fibn.append(0)
  fibn.append(1)
  while num!=2:

    c=a+b
    a=b
    b=c
    fibn.append(c)
    num=num-1
  return fibn

number=int(input())

fibn=[]

print(' '.join(map(str,fib(number))))
