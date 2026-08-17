#11. Extract values between quotation marks

s=input("Enter a string:")
result=""
inside=False

for ch in s:
    if ch=='"':
        inside=not inside
        continue
    if inside:
        result=result+ch

print("Extracted:",result)


#12.Convert snake case string to camel case

s=input("Enter a string:")
parts=s.split("_")
camel=parts[0]+"".join(word.capitalize()for word in parts[1:])
print("Camel case:",camel)


#13.Determine leap year

year=int(input("Enter a year:"))

if(year % 400==0) or (year % 4==0 and year %100 !=0):
   print(year,"is a Leap Year")
else:
    print(year,"is NOT a Leap Year")

#14.Convert String to Datetime

from datetime import datetime

s=input("Enter a date string(dd-mm-yyyy):")
dt=datetime.strptime(s,"%d-%m-%Y")
print("Converted datetime:",dt)


#15.Count uppercase and lowercase letters

def count_case(s):
    upper=0
    lower=0
    for ch in s:
        if ch.isupper():
            upper+=1
        elif ch.islower():
            lower+=1
    return upper,lower

s=input("Enter a string:")
u,l=count_case(s)
print("Uppercase letters:",u)
print("Lowercase letters:",l)
    
         
