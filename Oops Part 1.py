Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Oops-Object oriented programming language
... #elements of oops
... 
... #class
... #object
... #data abstraction
... #data encapsulation
... #data inheritance
... #polymorphism
... 
... #class
... #blueprint of objects
... #objects
... #instance of class
... #instance-internal data model,reference of class
... #c=Calci()
... #calci=Calci()
... #calci
... #c=calci()
... #calci=calci()
... #Calci
>>> 
>>> class Calci:
...     def sub(self,a,b):
...         return a-b
... 
    
c=Calci()
c.sub(66,30)
36



#scope of variables

#class variabe
#local variable
#global variable
#instance variable

class Company:
    company_name="TCS"
    def emp1(self):
        print('emp1 is doing project x in',Company.company_name)
    def emp2(self):
        print('emp2 is doing project x in',Company.company_name)
    def emp3(self):
        print('emp3 is doing project x in',Company.company_name)

        
c=Company()
c.emp1
<bound method Company.emp1 of <__main__.Company object at 0x0000021656317230>>
c.emp2()
emp2 is doing project x in TCS
c.emp3()
emp3 is doing project x in TCS

Company.company_name="Infosys"

c.emp1()
emp1 is doing project x in Infosys
c.emp2()
emp2 is doing project x in Infosys
c.emp3()
emp3 is doing project x in Infosys


#local variable

class Student:
    def Arun(self):
        locvar='B.sc-Maths'
        print('Arun degree is',locvar)
    def Aruna(self):
        print('Aruna degree is',locvar)

        
c=Student()
c.Arun()
Arun degree is B.sc-Maths
c.Aruna()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    c.Aruna()
  File "<pyshell#52>", line 6, in Aruna
    print('Aruna degree is',locvar)
NameError: name 'locvar' is not defined

#global variable
gv='complex'
gv='steps'
class Complex:
    def House1(self):
        print('prakash is using',gv)
    def House2(self):
        print('surya is using',gv)
    def House3(self):
        print('sabari is using',gv)

        
s.Complex()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    s.Complex()
NameError: name 's' is not defined
c.Complex()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    c.Complex()
AttributeError: 'Student' object has no attribute 'Complex'

=========================================== RESTART: Shell ==========================================
#local variable
gv='steps'
class Flat:
    def house1(self):
        print('prakash is using',gv)
    def house2(self):
        print('surya is using',gv)
    def house3(self):
        print('tanish is using',gv)

        
c=Flat()
c.house1()
prakash is using steps
c.house2()
surya is using steps
c.house3()
tanish is using steps

#global variable

#Data abstraction

from abc import ABC,abstract method
SyntaxError: invalid syntax
from abc import ABC,abstractmethod
class Appliance
SyntaxError: expected ':'
class Appliance(ABC):
    def turn_on(self):
        pass

    
class Fan(Appliance):
    def turn_on(self):
        print('Fan is running')

        
class Light(Appliance):
    def turn_on(self):
        print('Light is glowing')

        
f=Fan()
f.turn_on()
Fan is running
l=Light()
l.turn_on()
Light is glowing

