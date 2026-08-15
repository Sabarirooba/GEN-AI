#1. Write a program to remove lowercase characters.

def remove_lowercase(input_string):
    return''.join([char for char in input_string if not char.islower()])
s=input('enter a string')
result=remove_lowercase(s)
print('after removing lowercase characters:',result)


#2.Write a program that reads a given expression and evaluate it.

expression=input('enter an expression:')
res=eval(expression)
print(res)


#3.Write a program to insert spaces between words starting with capital letters.

def add_space():
    text=input('enter a string:')
    for i in text:
        if i.isupper():
            print(' ',end='')
        print(i,end='')
    print()

add_space()


#4.Write a program to remove the parenthesis area in a string.

words=input('enter a string:')
result=''
inside= False

for ch in words:
    if ch=='(':
        inside= True
    elif ch==')':
        inside= False
    elif not inside:
        result=result+ch
print(result)


#5.Write a program to split a string with multiple delimiters.

text=input('enter a string:')

text=text.replace(","," ")
text=text.replace(";"," ")
text=text.replace(":"," ")

words=text.split()
print(words)

    
    
