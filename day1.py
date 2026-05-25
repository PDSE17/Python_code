#variable

a=10
print(a)
#print is used to print

b=10
print(b)


#id is used to show address of variable in python
print(id(a))
print(id(b))
#hence it is proven that python work on values and same value points to the same address 
# memory is also same not required unnecessarily



#example
a=20
b=a
a=30
print(a,b)
print(id(a),id(b))


a=20
b=20
print(a,b)
print(id(a),id(b))


a=input("enter the number: ")
print(a)
print(type(a))
#by default the type is string 


a=int(input("enter the number:"))
print(a)
print(type(a))


