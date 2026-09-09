n=int(input())
a=n%3==0
b=n%5==0
result=["divisible neither","divisible by 3 but not 5","divisible by 5 but not 3","divisiible by both 3 and 5"][a+2*b]
print(result)
