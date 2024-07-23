
num1 = 22               # num1(int)
num2 = 9.81             # num2(float)
num3 = num1 + num2
    # num1 --> int --> float (temp converted implicitly)
    # num2 --> float
    # num3 --> float
print("num3 =", num3)
print("type of num3 =", type(num3))

var1 = True             # True=1
var2 = 40
var3 = var1 + var2      # bool->int (1) + int (40)
print("var3 =", var3)   # 41
print("type of var3 =", type(var3)) # int

num = 300
string = "War"
# result = string + num       # Error: int cannot be auto-converted to str
result = string + str(num)    # str(int) --> str (explicit type conversion)
        # string can be added/concat to another string
print("result =", result)
print("type of result =", type(result)) # int

s = "Nilesh"
flag = bool(s)          # bool(str) --> bool (explicit type conversion)
    # string to bool -- if string is empty --> False.
    # if string not empty --> True.
print("flag =", flag)
print("type of flag =", type(flag))

pi = 3.14
num = 7
res = num + int(pi)     # explicit conversion from float to int (.14 data is lost)
print("res =", res)
print("type of res =", type(res))

# type conversion functions
#   int(), float(), bool(), str(),
#   list(), tuple(), set(), dict() <-- advanced conversion fns
