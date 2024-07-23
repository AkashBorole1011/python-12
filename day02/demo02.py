
# In Java,
# String s1 = "One";

# In Python -- Type Hinting
# var: type = value
# Type Hinting makes code more readable to other developers/teammates.
# Type Hinting helps IDEs and type checkers to check the code and provide intellisense

s1: str = "One"
print("s1 =", s1)
print("type of s1 =", type(s1))

s2: int = 2
print("s2 =", s2)
print("type of s2 =", type(s2))

s3: float = 3.15
print("s3 =", s3)
print("type of s3 =", type(s3))

# Actual type is inferred at runtime depending on value assigned to the variable.
# This example, num is int (because 123 value is assigned)
# Programmer should not assign wrong type hint. But can be given.,
num: str = 123  # IDE WARNING: Expected type 'str', got 'int' instead
print("num =", num)
print("type of num =", type(num))
print("addr of num =", id(num))

num: float = 3.14
print("num =", num)
print("type of num =", type(num))
print("addr of num =", id(num))

