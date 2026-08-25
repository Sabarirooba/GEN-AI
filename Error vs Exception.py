Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Error vs Exception

#Error
#Error means misbehaved part of a python program
#error means unintentional mistake which stops the program execution
#it never allows the program run without correcting the error

import rooba
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    import rooba
ModuleNotFoundError: No module named 'rooba'
import dms
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    import dms
ModuleNotFoundError: No module named 'dms'
import ASSIGNMENT 1TO5
SyntaxError: invalid decimal literal
import calci
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    import calci
ModuleNotFoundError: No module named 'calci'
int(input('enter a value:'))
enter a value:rooba
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    int(input('enter a value:'))
ValueError: invalid literal for int() with base 10: 'rooba'
'2'+9
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    '2'+9
TypeError: can only concatenate str (not "int") to str
import.builtins
SyntaxError: invalid syntax

#Exception
#An unwanted or an unexpected event which disrupts the program of a logic
#it checks for alternate code against found exception

#types of error
#syntex error
#runtime error

#Reasons
#when inappropriate values are given
#when inadequate values are given
#when program is uneven

#Error
#it cannot be identified
#it cannot be tolerated
#it cannot be followed
#it cannot be corrected
#it cannot be controlled

#Exception
#it can be identified
#it can be tolerated
#it can be followed
#it can be corrected
#it can be controlled

#Exception handler components
#try block
#exception block
#finally block

3/0
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    3/0
ZeroDivisionError: division by zero
try:
    3/0
except:
    print('check input values')

    
check input values

#try block
#it checks for the errored part of program logic
#it check for critical statement of the program
#if it finds an error then it calls the except block

try
SyntaxError: expected ':'
try:
    4/2
except:
    print('check input values')

    
2.0
>>> 
>>> #except block
>>> #it will be activated only when try block find an error
>>> #except block usually checks for an alternate code against found exception
>>> #if alternate code is available then it returns patch worked output
>>> #if not it throws an error
>>> 
>>> #Finally block
>>> #it is a must execute code block
>>> #this block usually closes all opened functions/networked functions
>>> 
>>> try:
...     3/0
... except:
...     ('Dear user kindly check the input values')
... finally('------End------')
SyntaxError: expected ':'
>>> try:
...     4/0
... except:
...     ('Dear user kindly check the input values')
... finally:
...     ('-----END-----')
... 
...     
'Dear user kindly check the input values'
'-----END-----'
