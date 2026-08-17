#6. Adverbs and their positions

s=input('Enter a string:')
words=s.split()
position=0

for word in words:
    if word.endswith('ly'):
        print('adverb:',word,'position:',position)
    position=position+1


#7.Case-insensitive string replacement

s=input('Enter a string:')
x=input('Enter a key:')
s=s.split()
result=''

for i in s:
    if i.lower()=='world':
        result=result+x+' '
    else:
        result=result+i+' '

print('Result:',result)


#8.Split a string at uppercase letters

s=input('Enter a string:')
result=''
for i in range(len(s)):
    if s[i].isupper()and i !=0:
        result+=' '
    result +=s[i]

print(result)


#9.Remove everything except alphanumeric characters

s=input('Enter a string:')
result=''
for char in s:
    if char.isalnum():
        result=result+char

print('After removing:',result)


#10.Remove all white spaces

s=input('Enter a string:')
result=''
for i in s:
    if i !=' ':
        result=result+i

print(result)        
        
        
                                           

               
    
