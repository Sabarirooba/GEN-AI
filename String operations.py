Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'sabari rooba'.capitalize()
'Sabari rooba'
'SaBari ROoba'.casefold()
'sabari rooba'
'saBaRi Rooba'.lower()
'sabari rooba'
'sabari rooba'.upper()
'SABARI ROOBA'

'sabari rooba'.find('i')
5
'sabari rooba'.index('i')
5
'sabari rooba'.center(25)
'       sabari rooba      '
'sabari rooba'.ljust(25)
'sabari rooba             '
'sabari rooba'.rjust(25)
'             sabari rooba'
'250'.zfill(9)
'000000250'
'250'.center(8)
'  250   '
'250'.center(9,'*')
'***250***'
'250'.ljust(9,'*')
'250******'
'250'.rjust(9,'*')
'******250'
'   sabari rooba  '.strip()
'sabari rooba'
'   sabari rooba'.lstrip()
'sabari rooba'
'sabari rooba   '.rstrip()
'sabari rooba'


'sabari rooba'.count(a)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    'sabari rooba'.count(a)
NameError: name 'a' is not defined
'sabari rooba'.count('a')
3
'sabari rooba'.endswith('i')
False
'sabari rooba'.startswith('s')
True
'sabari rooba'.join('123')
'1sabari rooba2sabari rooba3'
'-'.join(['sabari','rooba','surya'])
'sabari-rooba-surya'
'sabari rooba'.partition('')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    'sabari rooba'.partition('')
ValueError: empty separator
'sabari rooba'.removeprefix('s')
'abari rooba'
'sabari rooba'.removesuffix('a')
'sabari roob'
>>> 'sabari rooba'.strip('s')
'abari rooba'
>>> 'sabari rooba'.title()
'Sabari Rooba'
>>> 'sabari rooba'.replace('r','R')
'sabaRi Rooba'
>>> 'sabari rooba'.split()
['sabari', 'rooba']
>>> 'sabari rooba'.isalpha()
False
>>> 'sabari rooba'.isalnum()
False
>>> 'sabari rooba'.isascii()
True
>>> 'sabari rooba'.isdecimal()
False
>>> 'sabari rooba'.isidentifier()
False
>>> 'sabari rooba'.islower()
True
>>> 'sabari rooba'.isnumeric()
False
>>> 'sabari rooba'.isprintable()
True
>>> 'sabari rooba'.isspace()
False
