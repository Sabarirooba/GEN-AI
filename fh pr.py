with open('rooba.txt', 'w+')as f:
 f.write('STUDY=Gen AI\\Course\\Tech panda\\rest')

with open('rooba.txt','r')as f:
 print(f.read(3))

with open('rooba.txt','r')as f:
 print (f.readline())

with open('rooba.txt','a')as f:
 f.writelines(['\\time\\money\\value'])

def rat():
    with open('rooba.txt','w+')as f:
        f.write('right angle triangle\n--------------\n')
        for i in range(1,6):
            for j in range(0,i):
                f.write(str(i))
            f.write('\n')

rat()

def irat():
    with open('rooba.txt','a') as f:
        f.write('Inverse right angle triangle\n------------\n')
        for i in range(6,0,-1):
            for j in range(1,i+1):
                f.write(str(j))
            f.write('\n')

irat()

with open('rooba.txt','r') as f:
    print(f.read())

def left_angle():
    with open('rooba.txt','a')as f:
        f.write('Left angle triangle\n-----------------\n')
        for i in range(1,6):
            for j in range(5,i,-1):
                f.write(str(i))
            f.write('\n')
left_angle()            
            

    

            
 





