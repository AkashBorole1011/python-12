
# Types of statements
# 1. Singleline statement
# 2. Multiline statement
# 3. Comment statement

# Comments -- Extra information about code
#   By programmer for programmer's reference
#   Ignored while execution by Python compiler/interpreter
#   Comments in Python starts with # symbol.

# Singleline statement
#   Statement ends with newline.
#   Optinally it can end with semicolon ;
num = 10
print("Number is", num)

# Multiline statement
# For better readability, we can continue a statement on next line using
#   Line continuation character (\)
result = 1 + 2 + 3 + 4 \
    + 5 + 6 + 7 + 8 + 9 + 10
print("Addition is", result)

# To write multiple singleline statements on same line
#   The statement must end with semicolon
pi = 3.14;  print("PI is", pi)
