Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Inheritance

class Vehicle:
    def start(self):
        print('Vehicle started')

        
class Car(Vehicle):
    def drive(self):
        print('Car is driving')

        
v=Vehicle()
v.start()
Vehicle started
c=Car()
c.drive()
Car is driving
c.start()
Vehicle started

#Multiple inheritance

class Teacher:
    def teach(self):
        print('Teacher:Teaches subject')

        
class Singer:
    def sing(self):
        print('Singer:Sings soulful songs')

        
class Dancer:
    def dance(self):
        print('Dancer:Performs graceful dance')

        
class Student(Teacher,Singer,Dancer):
    def introduce(self):
        print('Student:I learn,sing and dance')

        
s=Student()
s.dance()
Dancer:Performs graceful dance
s.teach()
Teacher:Teaches subject
s.sing()
Singer:Sings soulful songs
s.introduce()
Student:I learn,sing and dance

#multilevel inheritance

class Company:
    def company_info(self):
        print("company:Microsoft")

        
class Department(Company):
    def department_info(self):
        print("Department:Software development")

        
class Employee(Department):
    def employee_info(self):
        print("Employee:Surya-Python developer")

        
emp=Employee()
emp.company_info()
company:Microsoft
emp.department_info()
Department:Software development
emp.employee_info()
Employee:Surya-Python developer
Employee:Surya-Python developer
SyntaxError: invalid syntax

SyntaxError: invalid syntax
SyntaxError: invalid syntax

#Hierarchical inheritance

class Bank:
    def bank_info(self):
        print('Bank:State Bank of India')

        
class SavingsAccount(Bank):
    def account_type:
        
SyntaxError: expected '('

class Bank:
    def bank_info(self):
        print('Bank:State Bank of India):
              
SyntaxError: unterminated string literal (detected at line 3)


=========================================== RESTART: Shell ==========================================
#Hierarchical inheritance
              
class Bank:
    def bank_info(self):
        print('Bank:State Bank of India')

        
class Savingsaccount(Bank):
    def account_type(self):
        print('Savingsaccount:Interest applied')

        
class currentaccount(Bank):
...     def account_type(self):
...         print('currentaccount:No interest,Unlimited transactions')
... 
...         
>>> class loanaccount(Bank):
...     def account_type(self):
...         print('loan account:Repayment with interest')
... 
...         
>>> s=Savingsaccount()
>>> c=currentaccount()
>>> l=loanaccount()
>>> 
>>> s.account_type()
Savingsaccount:Interest applied
>>> s.bank_info()
Bank:State Bank of India
>>> 
>>> c.account_type()
currentaccount:No interest,Unlimited transactions
>>> c.bank_info()
Bank:State Bank of India
>>> 
>>> l.account_type()
loan account:Repayment with interest
>>> l.bank_info()
Bank:State Bank of India
