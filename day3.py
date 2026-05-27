# day 3 code


#and
num1=10
num2=20
print(num1 and num2)


#or
num1="hello"
num2=""
print(num1 or num2)
print(num2 or num1)


#not
num1=[]
print(not(num1))


#not
num1={}
print(not(num1))



#bitwise operator
# >>, <<, &, |, *


print(22 // 2)
print(22 >> 1)


# identity operator
# is , is not



name=10
name1=10
print(name == name1) #value


#example 1
name="prasanjeet"
name1="hello"
print(name == name1) #value | address
print(id(name1))
print(id(name))


#example 2
num1=-7
num2=-7

print(num1 == num2)
print(num1 is num2)

print(id(num1))
print(id(num2))


#example 3
num1=10
num2=10.0
print(num1==num2)
print(num1 is num2)
print(num1 is not num2)
print(id(num1))
print(id(num2))


# if -5 to 256---> same memory



# conditional statements

# if

num1=10
num2=20
if num1 < num2:
    print(True)


# if else
num1=int(input("enter the num1: "))
if num1:
    print("number: ",num1)
else:
    print("zero",num1)


# if elif else
age=int(input("enter the number: "))
if age==18:
    print("your age is: ",age)
elif age >18:
    print("you are greater than 18: ",age)
else:
    print("you are less than 18: ",age)


#example 1
marks=int(input("enter the marks: "))
if marks > 90 and marks < 100:
    print(" grade A")
elif marks < 90 and marks > 75:
    print(" grade B")
elif marks < 75 and marks > 35:
    print("grade C")
else:
    print("fail")



#example 2
num=int(input("enter the number: "))
if num % 2==0:
    print("even")
else:
    print("odd")



# loops

# for loop

for i in range(5):
    print(i)

for i in range(1,11):
    print(i) 


#list 
l=[11,12,13,14]
print(len(l))
for i in range(4):
    print(l[i])


for i in range(len(l)):
    print(l[i])

for i in l:
    print(i)    



#while

num1=int(input("enter the number: "))
i=0
while i < num1:
    print(i)
    i +=1

# list
l=[10,11,12,13,14,15]
while i < len(l):
    print(l[i])
    i +=1



#example 1
d={'name':'prasanjeet','age':20,'phone':"942132"}
l=d.keys()
print(l)

for i in range(len(d.keys())):
    print(l)


#example 2
l=[10,[11,12,13,14]]
print(l[1])

for i in l[1]:
    print(i)

    # print(" second approach")

for i in range (2,len(l[1])):
    print(l[1][i])
    


# break
for i in range(5):
    if i==2:
        break
    print(i)


# continue
i=0
while True:
    print(i)
    if i==5:
        break
    else:
     i +=1
     continue       



# pass
i=0
while True:
    print(i)
    if i ==4:
        pass
    if i==5:
        break
    else:
     i +=1
     continue       



    