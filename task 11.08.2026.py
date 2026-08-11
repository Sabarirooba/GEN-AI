print(' --------------------Factors------------------------')

def find_factors(n):
    factors=[]
    for i in range(1,n+1):
        if n%i==0:
            factors.append(i)
    return factors

num1=126
num2=245
num3=754

print('factors of',num1,':',find_factors(num1))
print('factors of',num2,':',find_factors(num2))
print('factors of',num3,':',find_factors(num3))

print('---------------------Amicable number------------------')

def is_amicable(x,y):
    sum1=0
    sum2=0
    for i in range(1,x):
        if x%i==0:
         sum1+=i
    for j in range(1,y):
        if y%j==0:
         sum2+=j
    return sum1==y and sum2==x
num1=int(input('enter number 1:'))
num2=int(input('enter number 2:'))

if is_amicable(num1,num2):
    print(num1,'and',num2,'are Amicable')
else:
    print(num1,'and',num2,'are Not Amicable')
    
'---------------------------Armstrong Number-----------------------'

def is_armstrong(n):
    digits=str(n)
    power=len(digits)
    total=sum(int(d)**power for d in digits)
    return total==n
num=int(input('enter a number: '))

if is_armstrong(num):
    print(num,'is an Armstrong Number')
else:
    print(num,'is Not an Armstrong Number')
    
    


