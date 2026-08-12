Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math
dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fma', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
math.cbrt(64)
4.0
math.sqrt(49)
7.0
math.ceil(13.6)
14
math.floor(-9)
-9
math.floor(-9.9)
-10
math.floor(7)
7
math.comb(5,2)
10
math.perm(5,2)
20
math.lcm(5,3)
15
math.gcd(20,24)
4
math.degrees(200)
11459.155902616465
math.radians(14578.1553)
254.43680885206172
254.43680885206172
254.43680885206172
math.fabs(-36)
36.0
math.factorial(7)
5040
math.fmod(30,3)
0.0
math.fsum(30,20)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    math.fsum(30,20)
TypeError: math.fsum() takes exactly one argument (2 given)
math.fsum([30,20])
50.0
math.isqrt(49)
7
math.pow(25,5)
9765625.0
math.pow(6,6)
46656.0
math.pow(6,2)
36.0

#Recursive function
#If a function calls itself repeatedly inside a single cell.

def fac
SyntaxError: expected '('

def fact(n):
    if n==0
    
SyntaxError: expected ':'
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print fact(5)
SyntaxError: invalid syntax
faSyntaxError: expected ':'
SyntaxError: invalid syntax

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
fact(5)
SyntaxError: invalid syntax
def fact(n)
SyntaxError: expected ':'
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))
SyntaxError: invalid syntax


def fact
SyntaxError: expected '('


def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

    
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))
SyntaxError: invalid syntax







#Lambda function
#Anonymous function/nameless function/onetime function

#RULES
#never use def keyword(use only def keyword)
#never use print/elif/return

add=lambda a,b,c:a+b+c
add(30+20+20)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    add(30+20+20)
TypeError: <lambda>() missing 2 required positional arguments: 'b' and 'c'
add=lambda a,b,c:a+b+c
print(add(5,10,5))
20
#Also called inline function
def chatbot(msg):
    if 'hello'in msg.lower():
        return 'Hi!How are you?'
    elif'bye'in msg.lower():
        return 'Goodbye!'
    else:
        return "I don't understand"
print(chatbot('hello'))
SyntaxError: invalid syntax
def chatbot(msg):
    if 'hello' in msg.lower():
        return ' hi! how are you?'
    elif 'bye' in msg.lower():
        return 'goodbye!'
    else:
        return "i don't understand'
    
SyntaxError: unterminated string literal (detected at line 7)
def chatbot(msg):
    if 'hello' in msg.lower():
        return ' hi! how are you?'
    elif 'bye' in msg.lower():
        return 'goodbye!'
    else:
        return "i don't understand"
    print(chatbot('hello'))

    

>>> 
>>> 
>>> 
>>> def chatbot(msg):
...     if 'hello' in msg.lower():
...         return ' hi! how are you?'
...     elif 'bye' in msg.lower():
...         return 'goodbye!'
...     else:
...         return "i don't understand"
...     print(chatbot('hello'))
... 
...     
>>> def chatbot(msg):
...     if 'hello' in msg.lower():
...         return ' hi! how are you?'
...     elif 'bye' in msg.lower():
...         return 'goodbye!'
...     else:
...         return "i don't understand"
...     print(chatbot('hello'))
... 
...     
>>> 
>>> 
>>> 
>>> 
