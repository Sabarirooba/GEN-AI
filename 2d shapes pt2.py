oval=[(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(3,1),(3,8),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7)]
def oval_():
    for i in range(1,5):
        for j in range(1,9):
            if(i,j)in oval:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()


trapezium=[(1,3),(1,4),(1,5),(1,6),(2,2),(2,7),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7)]
def trapezium_():
    for i in range(1,5):
        for j in range(1,8):
            if(i,j)in trapezium:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()


rectangle=[(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(2,2),(2,7),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7)]
def rectangle_():
    for i in range(1,5):
        for j in range(1,8):
            if(i,j)in rectangle:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()


parallelogram=[(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(2,2),(2,7),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7)]
def parallelogram_():
    for i in range(1,5):
        for j in range(1,9):
            if(i,j)in parallelogram:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()


while True:
    print('enter available choices:')
    print('1.oval')
    print('2.trapezium:')
    print('3.rectangle:')
    print('4.parallelogram:')

    choice=int(input('enter your choice:'))
    if choice==1:
        oval_()
    elif choice==2:
        trapezium_()
    elif choice==3:
        rectangle_()
    elif choice==4:
        parallelogram_()
    else:
        print('enter valid choice')


        
