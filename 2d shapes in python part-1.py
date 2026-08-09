square=[(1,3),(1,4),(1,5),(1,6),(1,7),(2,3),(2,7),(3,3),(3,7),(4,3),(4,7),(5,3),(5,4),(5,5),(5,6),(5,7)]
for i in range(1,9):
    for j in range(1,9):
        if(i,j)in square:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


circle=[(1,4),(1,5),(1,6),(1,7),(2,3),(2,7),(3,3),(3,7),(4,3),(4,7),(5,5),(5,6)]
for i in range(1,9):
    for j in range(1,9):
        if(i,j)in circle:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


semi_circle=[(2,6),(2,7),(2,8),(2,9),(3,4),(3,10),(4,4),(4,12),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10),(5,11),(5,12)]
for i in range(1,8):
    for j in range(1,13):
        if(i,j)in semi_circle:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

triangle=[(1,6),(2,5),(2,7),(3,4),(3,8),(4,3),(4,9),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10)]
for i in range(1,6):
    for j in range(1,11):
        if(i,j)in triangle:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


pentagon=[(1,5),(2,4),(2,6),(3,4),(3,7),(4,4),(4,6),(5,5),(5,6)]
for i in range(1,6):
    for j in range(1,8):
        if(i,j)in pentagon:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()        
     
    

    
            
            

    

    





     
