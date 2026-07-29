Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Tuple
>>> 
>>> #Enclose with()
>>> #Tuple values are ordered collection
>>> #tuples values are indexed
>>> #tuple values support duplicates
>>> #tuple values are immutable
>>> 
>>> 
>>> s=('computer','science','computer','science')
>>> 
>>> type(s)
<class 'tuple'>
>>> 
>>> s.count('science')
2
>>> s.index('computer')
0
>>> s
('computer', 'science', 'computer', 'science')
>>> 
>>> s=list(s)
>>> s
['computer', 'science', 'computer', 'science']
>>> 
>>> s.append('maths')
s
['computer', 'science', 'computer', 'science', 'maths']

s=tuple(s)
s
('computer', 'science', 'computer', 'science', 'maths')
s1=15+25+35
s
('computer', 'science', 'computer', 'science', 'maths')
s1
75
s1=(15,25,35)
s
('computer', 'science', 'computer', 'science', 'maths')
s1
(15, 25, 35)

s=s+s1

s
('computer', 'science', 'computer', 'science', 'maths', 15, 25, 35)
