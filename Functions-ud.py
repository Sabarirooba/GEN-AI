#User defined functions
name='rooba'

def name_rat():
    for i in range(0,len(name)):
        for j in range(0,i+1):
            print(name[i],end=' ')
        print()     

        

name_rat()

name=input('enter name:')
def name_rat():
    for i in range(0,len(name)):
        for j in range(0,i+1):
            print(name[i],end=' ')
        print()

name_rat()

def name_irat():
    for i in range(len(name),0,-1):
        for j in range(0,i+1):
            print(name[i-1],end=' ')
        print()

name_irat()

def name_pyramid():
    for i in range(1,6):
        for j in range(5,i,-1):
            print('',end=' ')
        for k in range(0,i):
            print(name[i],end=' ')
        print()

name_pyramid()

print('available choices')
print('-----------------')
print('1.name rat')
print('2.name irat')
print('3.name pyramid')

choice=int(input('enter your choice:'))
if choice==1:
    name_rat()
elif choice==2:
    name_irat()
elif choice==3:
    name_pyramid()
else:
    print('enter valid choice')


    
        

        





        
        





        
