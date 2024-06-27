#add number

def add_number(a,b):
    return a+b

#calling the rfunctuon
print(add_number(3,4))


def fun():
    print("Hello")
    
fun()

def sum_all(*num):
    return sum(num)
print(sum_all(1,2,3,4,5))



#Function with keyword Argument
def display_info(**kwargs):
    for key , values in kwargs.items():
        print(f"{key}:{values}")
        
display_info(name="DEep",age = 21 , city = "Patna") 


# Lambda

sq = lambda x : x*x
print(sq(5))

number  =  [1,2,3,4,5]
squ  = list(map(lambda s: s*s, number))

print(squ)


even_number = [1,2,3,4,6,5,7,8]

ev = list(filter(lambda e : e%2==0,even_number))
print(ev)


# Erroe  Handling

try:
    result = 10/0
except ZeroDivisionError:
    print("cannot divide by zero")
    
    
    
try:
    result = 10/2
except ZeroDivisionError:
    print("cannot divide by zero") 
else:
    print("Successfully")   
    
    
def check_positive(num1):
    if num1<=0:
        raise ValueError("number must be positive")

try:
    check_positive(-5)
except ValueError as e:
    print(e)
    