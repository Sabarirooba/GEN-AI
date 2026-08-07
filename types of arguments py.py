Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

#Types of arguments in user defined function

#Default argument
#Positional argument
#Keyword argument
#Arbitrary argument


#Default argument-funtions to be created with parameters and default values

def student_info(name='rooba',city='chennai',mark=98,subject='maths'):
       print(f'name is {name} city is {city} mark is {mark} subject is {subject}')

       
student_info()
name is rooba city is chennai mark is 98 subject is maths

student_info('surya','chennai','99','science')
name is surya city is chennai mark is 99 subject is science

#Positional argument













-

=========================================== RESTART: Shell ==========================================
#Positional argument-User/developer has to remember the order of parameters so that he can send argument

student_info('divya','98','madurai','social')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    student_info('divya','98','madurai','social')
NameError: name 'student_info' is not defined

=========================================== RESTART: Shell ==========================================
def student_info(name='rooba',city='chennai',mark=98,subject='maths'):
       print(f'name is {name} city is {city} mark is {mark} subject is {subject}')

student_infodef student_info(name='rooba',city='chennai',mark=98,subject='maths'):
       print(f'name is {name} city is {city} mark is {mark} subject is {subject}')
       
SyntaxError: invalid syntax
student_info('divya','98','madurai','social')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    student_info('divya','98','madurai','social')
NameError: name 'student_info' is not defined

=========================================== RESTART: Shell ==========================================
#Positional argument-User/developer has to remember the order of parameters so that he can send argument
>>> 
>>> def student_info(name='divya',city='chennai',mark='96',subject='social')
SyntaxError: expected ':'
>>> def student_info(name='divya',city='chennai',mark='96',subject='social'):
...     print(f'name is {name} city is {city} mark is {mark} subject is {subject}')
... 
...     
>>> student_info()
name is divya city is chennai mark is 96 subject is social
>>> student_info('divya','96','chennai','social')
name is divya city is 96 mark is chennai subject is social
>>> student_info()
name is divya city is chennai mark is 96 subject is social
>>> 
>>> #Keyword argument
>>> student_info()
name is divya city is chennai mark is 96 subject is social
>>> student_info(mark='99')
name is divya city is chennai mark is 99 subject is social
>>> 
>>> 
>>> #Builtin functions
>>> #represented in purple colour
>>> #also called readymade function/steady state function/shipped function
>>> 
>>> abs(-11)
11
bin(19)
'0b10011'
bool(0)
False
bool(23)
True
chr(24)
'\x18'
chr(95)
'_'
chr(65)
'A'
divmod(24,5)
(4, 4)
for i in 'sabari rooba':
    print(i)
for i in enumerate('sabari rooba')
SyntaxError: invalid syntax
for i in 'sabari rooba':
    print(i)
    for i in enumerate('sabari rooba')
    
SyntaxError: expected ':'
for i in 'sabari rooba':
    print(i)
for i in enumerate('sabari rooba'):
    
SyntaxError: invalid syntax

for i in ('sabari rooba'):
    print(i)
    for i in enumerate('sabari rooba'):
        print()

        
s












a












b












a












r












i












 












r












o












o












b












a












sorted('rooba')
['a', 'b', 'o', 'o', 'r']
sorted('rooba')[::-1]
['r', 'o', 'o', 'b', 'a']
round(2.3)
2
ord('a')
97
eval('20'+'50')
2050
eval('20+50')
70
exit()
len('rooba')
5
min(1,2,3,4)
1
max(1,2,3,4,)
4
sum([10,20,30])
60
pow(6,2)
36
