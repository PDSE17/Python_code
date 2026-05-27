# day2 code

a=10
b=10
print(a,b)
print(id(a))
print(id(b))
print(type(a))
print(type(b))
# if the values of the two variables are same then they will point to the same memory location 
#python work on values 
#check the id of both the variables to verify it


#integer
a=10
print(a)
print(type(a))

#float
b=10.10
print(b)
print(type(b))


#string
c="prasanjeet das"
print(c)
print(type(c))

#boolean
d=True
print(d)
print(type(d))


# input function is used to take input from user
# output function used to print the values of variables
num=input("enter the number: ")
print(num)
print(type(num))
print(int(num)+10) #both have type integer
print(num + str(10)) #both have type string


num=int(input("enter the number: "))
print(num)
print(type(num))

# by default it is a string no need to add str
name=input("enter the number: ")
print(name)
print(type(name))


#operators


# uniary------> works on one operand 
not(10)

# binary------> works on two operands 
print(10 + 20)



#arithmetic operator
# + - * / % * * //

# +, -
a=10
b=20
print(a + b)
print(a - b)

# *
c=10
d=5
print(c * d)

# /
num_1=10
num_2=2
print(num_1 / num_2)


# //
num_3=30
num_4=10
print(num_3 // num_4)

# %
f=5
g=4
print(f % g)

# * *
num_5=4
num_6=3
print(num_5 ** num_6)


# example even or odd

num1=int(input("enter the num1: "))
if (num1 % 2)==0:
    print("even")
else:
    print("odd")




# Relation operator
# ==, >, <, >=, <=, +=, !=
# true or false 

# ==
num1=10
num2=11
print(num1 == num2) #equal to


# <
num1=10
num2=11
print(num1 < num2) #less than

#  >
num1=10
num2=11
print(num1 > num2) #greater than


# <=
num1=10
num2=12
print(num1 <=num2) #less than equal to

# >=
num1=10
num2=10
print(num1 >= num2) #greater than equal to

# !=
num1=100
num2=200
print(num1 != num2) #not equal to


# assignment operator
# =, +=, -=, *=, /=, //=, %=

# = ---> used to declare a variable

# += assignment operator
a=10
b=a+20
print(a,b)

a=10
a+=20
print(a)


# -=
a=10
b=a-2
print(a,b)

a=10
a-=2
print(a)

# *=
a=20
b=a*2
print(a,b)

a=20
a*=3
print(a)



# /=
a=10
b= a/2
print(a,b)



a=10
a/=2
print(a)


#//=
a=20
b=a//3
print(a,b)


a=20
a//=3
print(a)


# %=
a=20
b=a%3
print(a,b)

a=20
a%=3
print(a)



#logical operator

# and, or, and not
# and

#number---> +ve,-ve --->true
# zero(0)----> false


#string---> 
"hello"#--->true
"  "#--->true
""#---->false


#and--->read both a and b
a=10
b=20
print(a and b)


#or---->read only one 
a=10
b=-20
print(a or b)


#not
a=10
print(not(a))


name1="hello"
name2=""
print(name1 and name2) #blank output
print(name1 or name2 ) #hello output
print(not(name1))


# questions on logical operators


# Q1
a=10
b=20
print(a>5 and b>15)



# Q2
a=5
b=2
print(a>10 or b<5)


# Q3
a=10
print(not(a>5))


# Q4
age=19
has_id=True
print(age>= 18 and has_id)


# Q5
username = "admin"
password = "1234"
print(username == "admin" and password == "admin")


# Q6
x = 5
print(x > 2 and x < 10)


# Q7
print(True and False or True)


# Q8
print(not True and False)


# Q9
a = 0
print(a and 10)
print(a or 10)


# Q10
x = 5
y = 10
z = 15
print(x < y and y < z)
print(x > y or z > y)

