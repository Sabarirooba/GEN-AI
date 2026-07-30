Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#SET

#Set is enclosed with {values} with braces.

name={'sabari','rooba'}
name
{'sabari', 'rooba'}
type(name)
<class 'set'>

#Set is an unordered collection of data
#Set values are unindexed
#Set never supports duplicates
#Popping allowed from beginning to end


fruits={'apple','mango','grapes'}
fruits
{'mango', 'grapes', 'apple'}


numbers={25,35,45,65}
numbers
{65, 25, 35, 45}

x={2,4,6,8,10}
y={3,6,8,12,9}
x
{2, 4, 6, 8, 10}
y
{3, 6, 8, 9, 12}

x.add(14)
x
{2, 4, 6, 8, 10, 14}

y.add(15)
>>> y
{3, 6, 8, 9, 12, 15}
>>> 
>>> x.difference(y)
{2, 10, 4, 14}
>>> 
>>> y.difference(x)
{9, 3, 12, 15}
>>> 
>>> x.difference_update(y)
>>> y.difference_update(x)
>>> x
{2, 4, 10, 14}
>>> y
{3, 6, 8, 9, 12, 15}
>>> 
>>> x.add(16)
>>> x
{16, 2, 4, 10, 14}
>>> y.add(18)
>>> y
{18, 3, 6, 8, 9, 12, 15}
>>> 
>>> x.add(6)
>>> x
{16, 2, 4, 6, 10, 14}
>>> x.add(8)
>>> x
{16, 2, 4, 6, 8, 10, 14}


x.difference(y)
{2, 4, 10, 14, 16}
y.difference(x)
{3, 9, 12, 15, 18}

x.difference_update(y)
x
{16, 2, 4, 10, 14}
y.difference_update(x)
y
{18, 3, 6, 8, 9, 12, 15}
x
{16, 2, 4, 10, 14}
y
{18, 3, 6, 8, 9, 12, 15}
y.clear(18)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    y.clear(18)
TypeError: set.clear() takes no arguments (1 given)
y.remove(18)
y
{3, 6, 8, 9, 12, 15}
x
{16, 2, 4, 10, 14}
y.remove(15)
y
{3, 6, 8, 9, 12}
x
{16, 2, 4, 10, 14}
x.remove(16)
x
{2, 4, 10, 14}
x.add(6)
x
{2, 4, 6, 10, 14}
y
{3, 6, 8, 9, 12}
x.remove(14)
x
{2, 4, 6, 10}
x.add(12)
x
{2, 4, 6, 10, 12}
y
{3, 6, 8, 9, 12}


x
{2, 4, 6, 10, 12}
y
{3, 6, 8, 9, 12}

x.union(y)
{2, 3, 4, 6, 8, 9, 10, 12}
x.intersection(y)
{12, 6}

x.isdisjoint(y)
False
x.issubset(y)
False
x.issuperset(y)
False
x.pop()
2
x.pop()
4

x
{6, 10, 12}
y
{3, 6, 8, 9, 12}
y.pop()
3
y.pop()
6
y
{8, 9, 12}
x
{6, 10, 12}
y
{8, 9, 12}

x.update(y)
x
{6, 8, 9, 10, 12}
y
{8, 9, 12}
y.update(x)
y
{6, 8, 9, 10, 12}
x
{6, 8, 9, 10, 12}
x.symmetric_difference(y)
set()
x
{6, 8, 9, 10, 12}
y
{6, 8, 9, 10, 12}



#Dictionary

#Dictionary is not indexed
#Dictionary contains ordered collection of data items
#Dictionary follows{key:value}as a paired items
#Dictionary does not allow dublicate values
#Popping is allowed

bike={'brand'='yamaha','model'='r15 v4','type'='sports','price'='180000'}
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
bike={'brand':'yamaha','model':'r15 v4','type':'sports','price':'180000'}
bike
{'brand': 'yamaha', 'model': 'r15 v4', 'type': 'sports', 'price': '180000'}

type(bike)
<class 'dict'>
bike('brand)
     
SyntaxError: unterminated string literal (detected at line 1)
bike('brand')
     
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    bike('brand')
TypeError: 'dict' object is not callable
bike['brand']
     
'yamaha'
bike['type']
     
'sports'
bike['price']
     
'180000'
bike.keys()
     
dict_keys(['brand', 'model', 'type', 'price'])
bike.values()
     
dict_values(['yamaha', 'r15 v4', 'sports', '180000'])
bike.pop(model)
     
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    bike.pop(model)
NameError: name 'model' is not defined
bike('model')
     
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    bike('model')
TypeError: 'dict' object is not callable
bike.pop('model')
     
'r15 v4'
bike.popitem()
     
('price', '180000')
