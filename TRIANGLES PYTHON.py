Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#row numbers left angle triangle
for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(i,end=' ')
    print()

    
        1 
      2 2 
    3 3 3 
  4 4 4 4 
5 5 5 5 5 
#column numbers left angle triangle
for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print((k+1),end=' ')
    print()

    
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 

#star pattern left angle triangle
for i in range(1,6):
    for j in range(5,i,-1):
...         print(' ',end=' ')
...     for k in range(0,i):
...         print('*',end=' ')
...     print()
... 
...     
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
>>> 
>>> #upper case row left angle triangle
>>> 
>>> for i in range(1,6):
...     for j in range(5,i,-1):
...         print(' ',end=' ')
...     for k in range(0,i):
...         print(chr(i+64),end=' ')
...     print()
... 
...     
        A 
      B B 
    C C C 
  D D D D 
E E E E E 
