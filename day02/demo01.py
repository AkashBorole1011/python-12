
num = 100
num = 200
print("num =", num)
print("type of num =", type(num)) # type() is a function
print("addr of num =", id(num)) # id() is a function
print("size of num =", num.__sizeof__()) # __sizeof__() is member function (OOP)

var = 9.81
var = 8.91
print("var =", var)
print("type of var =", type(var))
print("addr of var =", id(var))
print("size of var =", var.__sizeof__())

flag = True
flag = False
print("flag =", flag)
print("type of flag =", type(flag))
print("addr of flag =", id(flag))
print("size of flag =", flag.__sizeof__())

name = "James"
name = "Bond"
print("name =", name)
print("type of name =", type(name))
print("addr of name =", id(name))
print("size of name =", name.__sizeof__())

# sometimes, we need data that is not intended to be modified in the program.
# this is called as const or final data (in C or Java langauge)
# In Python, there is no final/const variable concept.
# Python developer follow convention to represent final/const variables.
# final var names are written in all caps.
PI = 3.1415 # By convention, PI is constant
# PI = 3.3333 # Programmer should not modify constants
print("PI =", PI)

c = 2 + 3j
print("c =", c)
print("type of c=", type(c))

str1 = 'Welcome to Python'
str2 = "Welcome to Sunbeam"
str3 = '''Python-12 Batch
Started on 22-Jul
Invite your friends if interested.
'''
print("str1 =", str1)
print("str2 =", str2)
print("str3 =", str3)

