T=int(input("enter testcases: "))
cases=[]
for i in range (0,T):
    case=int(input())
    cases.append(case)
print(cases)
for item in cases:
     sum=0
     for i in range (1,item):
          sum=sum+i
          if(sum>=item):
              print(i)
              break
