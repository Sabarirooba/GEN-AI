Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#DECISION MAKING STATEMENT OR CONDITIONAL STATEMENT

#IF
#IF....ELSE
#IF....ELSE....ELIF

#IF

#if the condition is satisfied it prints something, if does not it prints nothing.

x=10
if x>5:
    print('x is greater than 5')

    
x is greater than 5

#IF....ELSE

#if statement is satisfied then it returns IF BLOCK statements, if not then it returns ELSE BLOCK statements

x=3
if x>5:
    print('x is greater than 5')
    else('x is not greater than 5')
    
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: invalid syntax
x=3
if x>5:
    print('x is greater than 5')
    else:('x is not greater than 5')
    
SyntaxError: invalid syntax
x=3
if x>5:
    print('x is greater than 5')
else:
    print('x is not greater than 5')

    
x is not greater than 5

#IF....ELIF...ELSE
#if a single value to be checked with multiple test conditions.

x=5
if x>5:
    print('x is greater than 5')
elif x==5:
    print('x is equal to 5')
else x<5:
    
SyntaxError: expected ':'
x=5
if x>5:
    print('x is greater than 5')
elif x==5:
    print('x is equal to 5')
    
SyntaxError: multiple statements found while compiling a single statement
x=5
if x>5:
    print('x is greater than 5')
elif x==5:
    print('x is equal to 5')
    
SyntaxError: multiple statements found while compiling a single statement
x=5
if x>5:
    print('x is greater than 5')
elif x==5:
    print('x is equal to 5')
else:
    print('x is less than 5')

    
x is equal to 5

#NESTED IF
#if one test condition is given inside another.
x=10
if x>5:
if x%2==0:
    
SyntaxError: expected an indented block after 'if' statement on line 1
x=10
if x>5:
    if x%2==0
    
SyntaxError: expected ':'
x=10
if x>5:
    if x%2==0:
        print('x is greater than 5 and even')

        
x is greater than 5 and even


name='rooba'
if name=='rooba':
    print('name is correct')

    
name is correct


name='rooba'
mark='98'
if name=='rooba'and mark=='78':
    print('name and mark is matched')
else:
    print('name and mark is not matched')

    
name and mark is not matched

if mark>90:
    print('very good')
elif mark==90:
    print('good')
else mark<90:
    
SyntaxError: expected ':'
if mark>90:
    print('very good')
elif mark==90:
    print('good')
else mark!=90:
    
SyntaxError: expected ':'
if mark>90:
    print('very good')
elif mark==90:
    print('good')
else mark!=90:
    
SyntaxError: expected ':'
SyntaxError: expected ':'

if mark>90:
    print('very good')
elif mark==90:
    print('good')
else:
    print('fair')

    
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    if mark>90:
TypeError: '>' not supported between instances of 'str' and 'int'
mark='95'
if mark>'95':
    print('very good')
elif mark=='95':
    print('good')
else:
    print('fair')

    
good


#LOOPING STATEMENTS

#same set of actions repeated many times till n-1 times based on given condition.
#TYPES

#for loop
#while loop

#ITERATIVE STATEMENTS
#going through the elements of a given python collections(list,set,tuple,dict)using for loop, while loop.

for i in range(1,10):
    print(i)

    
1
2
3
4
5
6
7
8
9

for i in range (12,21):
    print(i,end=' ')

    
12 13 14 15 16 17 18 19 20 

for i in range(51,61):
    print(i)

    
51
52
53
54
55
56
57
58
59
60
for i in range(91,101):
    print (i,end=' ')

    
91 92 93 94 95 96 97 98 99 100 
for i in range(91,101):
    print(i)
    print(' ')

    
91
 
92
 
93
 
94
 
95
 
96
 
97
 
98
 
99
 
100
 
#print even numbers between 20 to 30

for i in range(20,31,2)
SyntaxError: expected ':'
for i in range(20,31,2):
    print(i,end=' ')

    
20 22 24 26 28 30 


for i in range(5,51):
    if i%5==0:
        print(i,'- is divisible by 5')
    else:
        print(i,'- is not divisible by 5')

        
5 - is divisible by 5
6 - is not divisible by 5
7 - is not divisible by 5
8 - is not divisible by 5
9 - is not divisible by 5
10 - is divisible by 5
11 - is not divisible by 5
12 - is not divisible by 5
13 - is not divisible by 5
14 - is not divisible by 5
15 - is divisible by 5
16 - is not divisible by 5
17 - is not divisible by 5
18 - is not divisible by 5
19 - is not divisible by 5
20 - is divisible by 5
21 - is not divisible by 5
22 - is not divisible by 5
23 - is not divisible by 5
24 - is not divisible by 5
25 - is divisible by 5
26 - is not divisible by 5
27 - is not divisible by 5
28 - is not divisible by 5
29 - is not divisible by 5
30 - is divisible by 5
31 - is not divisible by 5
32 - is not divisible by 5
33 - is not divisible by 5
34 - is not divisible by 5
35 - is divisible by 5
36 - is not divisible by 5
37 - is not divisible by 5
38 - is not divisible by 5
39 - is not divisible by 5
40 - is divisible by 5
41 - is not divisible by 5
42 - is not divisible by 5
43 - is not divisible by 5
44 - is not divisible by 5
45 - is divisible by 5
46 - is not divisible by 5
47 - is not divisible by 5
48 - is not divisible by 5
49 - is not divisible by 5
50 - is divisible by 5

flowers=['rose','lotus','sunflower','lily','orchid','marigold']

for i in flowers:
    print(i)

    
rose
lotus
sunflower
lily
orchid
marigold

for i in flowers:
    print i.startswith('l')
    
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
for i in flowers:
    if i.startswith('l')
    
SyntaxError: expected ':'
flowers=['rose','lotus','sunflower','lily','orchid','marigold']
for i flowers:
    
SyntaxError: multiple statements found while compiling a single statement
flowers=['rose','lotus','sunflower','lily','orchid','marigold']
for i in flowers:
    if i.startswith('l')
    
SyntaxError: expected ':'
flowers=['rose','lotus','sunflower','lily','orchid','marigold']
for i in flowers:
    if i.startswith('l'):
        print(i)

        
lotus
lily

for i in flowers:
    if i.endswith('d'):
        print(i)

        
orchid
marigold

for i in flowers:
    if len(i)==4:
        print(i)

        
rose
lily

for in flowers
SyntaxError: invalid syntax

for i in flowers
SyntaxError: expected ':'

for i in flowers:
    if i.endswith('e'):
    elif i.endswith('s'):
        
SyntaxError: expected an indented block after 'if' statement on line 2

for in flowers:
    
SyntaxError: invalid syntax

for i in flowers:
    if i.endswith('e'):
        print(i,' ')
    elif i.endswith('s'):
        print(i,' ')
    elif i.endswith('r'):
        print(i,' ')
    elif i.endswith('y'):
        print(i,' ')
    elif i.endswith('d'):
        print(i,' ')

        
rose  
lotus  
sunflower  
lily  
orchid  
marigold  


#for loop
    #CORM - checks once runs many time
    #for loop checks the condition once and runs the loops many times.
#while loop
    #checks the condition many times and runs the loop till the condition is true
    #it is mandate to give the incremental/decremental value



#FLOW CONTROL STATEMENT
#also acts like jumping statement
#break/continue/pass

for i in range(1,16)
SyntaxError: expected ':'

for i in range(1,16):
    i==15:
        
SyntaxError: invalid syntax

for i in range(1,16)
SyntaxError: expected ':'
for i in range(1,16):
    if i==15:
        break.
    
SyntaxError: invalid syntax

for i in range(1,16):
    if i==15:
        break
    print(i)

    
1
2
3
4
5
6
7
8
9
10
11
12
13
14

for i in range(1,30,3):
    if i==3:
        continue
    print(i)

    
1
4
7
10
13
16
19
22
25
28
#break
#it terminates the execution of a loop when a certain condition is met.
#continue
#it skips a particular value from the loop when certain condition is met and resumes the execution from the next element.

#task
#display numbers between 10 to 20 and skip number 15 and 18

for i in range(10,21):
    if i==15,18:
        
SyntaxError: invalid syntax

for i in range(10,21):
    if i==15 and 18:
        continue
    print(i)

    
10
11
12
13
14
16
17
18
19
20

for i in range(10,21)
SyntaxError: expected ':'

for i in range(10,21):
    if i==15 or 18:
        continue
    print(i)

    

for i in range(10,21):
    if i==15 or i==18:
        continue
    print(i)

    
10
11
12
13
14
16
17
19
20

names=['harsha','riya','surya','prakash','nila','kayal']

for i in names
SyntaxError: expected ':'
for i in names:
    if len(i)=5:
        
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
for i in names:
    if len(i)==5:
        print(i)

        
surya
kayal
for i in names:
    if len(i)!=5:
        print(i)

        
harsha
riya
prakash
nila


#PATTERNS PROGRAM USING FOR LOOP

#right angle triangle
for i in range(0,5):
    for j in range(0,i):
        print(i,end=' ')
        print()

        
1 
2 
2 
3 
3 
3 
4 
4 
4 
4 

for i in range(0,6):
    for j in range(0,i):
        print()

        















for i in range(0,6):
    for j in range(0,5):
        print()

        






























for i in range(0,8):
    for j in range(i+1):
        print(i,end=' ')
        print()

        
0 
1 
1 
2 
2 
2 
3 
3 
3 
3 
4 
4 
4 
4 
4 
5 
5 
5 
5 
5 
5 
6 
6 
6 
6 
6 
6 
6 
7 
7 
7 
7 
7 
7 
7 
7 
for i in range(0,8):
    for j in range(i+1):
        print(j,end=' ')
        print()

        
0 
0 
1 
0 
1 
2 
0 
1 
2 
3 
0 
1 
2 
3 
4 
0 
1 
2 
3 
4 
5 
0 
1 
2 
3 
4 
5 
6 
0 
1 
2 
3 
4 
5 
6 
7 
for i in range(0,8):
    for j in range(0,i+1):
        print(i,end=' ')
        print()

        
0 
1 
1 
2 
2 
2 
3 
3 
3 
3 
4 
4 
4 
4 
4 
5 
5 
5 
5 
5 
5 
6 
6 
6 
6 
6 
6 
6 
7 
7 
7 
7 
7 
7 
7 
7 
for i in range(1,8):
    for j in range(1,i+1):
        print(i,end=' ')
        print

        
1 <built-in function print>
2 <built-in function print>
2 <built-in function print>
3 <built-in function print>
3 <built-in function print>
3 <built-in function print>
4 <built-in function print>
4 <built-in function print>
4 <built-in function print>
4 <built-in function print>
5 <built-in function print>
5 <built-in function print>
5 <built-in function print>
5 <built-in function print>
5 <built-in function print>
6 <built-in function print>
6 <built-in function print>
6 <built-in function print>
6 <built-in function print>
6 <built-in function print>
6 <built-in function print>
7 <built-in function print>
7 <built-in function print>
7 <built-in function print>
7 <built-in function print>
7 <built-in function print>
7 <built-in function print>
7 <built-in function print>
for i in range(1,8):
    for j in range(1,i+1):
        print(j,end=' ')
        print

        
1 <built-in function print>
1 <built-in function print>
2 <built-in function print>
1 <built-in function print>
2 <built-in function print>
3 <built-in function print>
1 <built-in function print>
2 <built-in function print>
3 <built-in function print>
4 <built-in function print>
1 <built-in function print>
2 <built-in function print>
3 <built-in function print>
4 <built-in function print>
5 <built-in function print>
1 <built-in function print>
2 <built-in function print>
3 <built-in function print>
4 <built-in function print>
5 <built-in function print>
6 <built-in function print>
1 <built-in function print>
2 <built-in function print>
3 <built-in function print>
4 <built-in function print>
5 <built-in function print>
6 <built-in function print>
7 <built-in function print>
for i in range(1,8):
    for j in range(1,i+1):
        print(j,end=' ')
        print()

        
1 
1 
2 
1 
2 
3 
1 
2 
3 
4 
1 
2 
3 
4 
5 
1 
2 
3 
4 
5 
6 
1 
2 
3 
4 
5 
6 
7 
>>> for i in range(1,8):
...     for j in range(1,i+1):
...         print(j,end=' ')
...     print()
... 
...     
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6 
1 2 3 4 5 6 7 
>>> 
=========================================== RESTART: Shell ==========================================
