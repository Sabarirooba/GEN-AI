#16.Unique elements from list

def unique_list(lst):
    unique=[]
    for i in lst:
        if i not in unique:
            unique.append(i)
    return unique

print(unique_list([1,2,1,3,4,4]))


#17.Prime number check

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

print(is_prime(23))
print(is_prime(92))

#18.Even numbers from list

def print_even(lst):
    for i in lst:
        if i%2==0:
            print(i,end=" ")

print_even([11,22,33,42,50,96,20,10,99])


#19.Perfect number check

def is_perfect(n):
    sum_div= 0
    for i in range(1,n):
        if n%i== 0:
            sum_div += i
    return sum_div== n

print(is_perfect(32))
print(is_perfect(28))


#20.Reverse string word by word

def reverse_words(s):
    words=s.split()
    rev=words[::-1]
    return " ".join(rev)

print(reverse_words("Next month is september"))

    
