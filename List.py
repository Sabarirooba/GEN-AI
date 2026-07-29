Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Python Native datatypes / Python collections / Python Non-primitive datatypes

#primitive datatypes-string/float/int/complex/boolean

name='sabari rooba'
type(name)
<class 'str'>


#Non primitive datatypes-list/tuple/set/dict


#List

#Enclosed with[]
#It contains ordered collection of data items
#List values are indexed
#Values are mutable and changeble
#It supports duplicate values
#It contains heterogeneous values

flowers = ['rose','jasmine','lotus','lily','rose','sunflower']

type(flowers)
<class 'list'>
flowers
['rose', 'jasmine', 'lotus', 'lily', 'rose', 'sunflower']
flowers[0]
'rose'
flowers[3]
'lily'
flowers[0]==flowers[4]
True
flowers[0]
'rose'

flowers[0]='hibiscus'

flowers
['hibiscus', 'jasmine', 'lotus', 'lily', 'rose', 'sunflower']
flowers[:4]
['hibiscus', 'jasmine', 'lotus', 'lily']
flowers[2:]
['lotus', 'lily', 'rose', 'sunflower']
flowers[1:5]
['jasmine', 'lotus', 'lily', 'rose']


#list methods/list supporting functions/list operations


flowers
['hibiscus', 'jasmine', 'lotus', 'lily', 'rose', 'sunflower']

flowers.append('marigold')
flowers
['hibiscus', 'jasmine', 'lotus', 'lily', 'rose', 'sunflower', 'marigold']

car.clear()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    car.clear()
NameError: name 'car' is not defined. Did you mean: 'chr'?

flowers.clear()
flowers
[]
flowers.append('tulip')
flowers.append('lily')
flowers.append('rose')
flowers
['tulip', 'lily', 'rose']

flowers.extend('hibiscus','jasmine','lotus')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    flowers.extend('hibiscus','jasmine','lotus')
TypeError: list.extend() takes exactly one argument (3 given)
flowers
['tulip', 'lily', 'rose']
flowers.extend(['hibiscus','jasmine','lotus'])
flowers
['tulip', 'lily', 'rose', 'hibiscus', 'jasmine', 'lotus']

flowers.count('jasmine')
1
flowers.index('rose')
2
flowers.insert(3,'orchid')
flowers
['tulip', 'lily', 'rose', 'orchid', 'hibiscus', 'jasmine', 'lotus']

flowers.pop()
'lotus'
flowers
['tulip', 'lily', 'rose', 'orchid', 'hibiscus', 'jasmine']
flowers.pop(4)
'hibiscus'
flowers
['tulip', 'lily', 'rose', 'orchid', 'jasmine']

flowers.remove('jasmine')
flowers
['tulip', 'lily', 'rose', 'orchid']

flowers.reverse()
flowers
['orchid', 'rose', 'lily', 'tulip']

flowers.sort()
flowers
['lily', 'orchid', 'rose', 'tulip']


flowers
['lily', 'orchid', 'rose', 'tulip']
flowers duplicate=flowers
SyntaxError: invalid syntax
flowers Duplicate=flowers
SyntaxError: invalid syntax
flowers
['lily', 'orchid', 'rose', 'tulip']
flowers_dup=flowers
flowers
['lily', 'orchid', 'rose', 'tulip']
flowers_dup
['lily', 'orchid', 'rose', 'tulip']
>>> flowers_dup(1)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    flowers_dup(1)
TypeError: 'list' object is not callable
>>> flowers_dup[1]
'orchid'
>>> flowers_dup[1]='poppy'
>>> flowers
['lily', 'poppy', 'rose', 'tulip']
>>> flowers_dup
['lily', 'poppy', 'rose', 'tulip']
>>> dup=flowers.copy()
>>> flowers
['lily', 'poppy', 'rose', 'tulip']
>>> dup
['lily', 'poppy', 'rose', 'tulip']
>>> dup[2]='sunflower'
>>> flowers
['lily', 'poppy', 'rose', 'tulip']
>>> dup[3]
'tulip'
>>> dup[3]='prakash'
>>> dup
['lily', 'poppy', 'sunflower', 'prakash']
>>> flowers
['lily', 'poppy', 'rose', 'tulip']
