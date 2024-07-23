
# input circle radius and calculate its area
radius = float(input("Enter radius: "))

PI = 3.1415         # conventionally, all caps are const/final value
# area = PI * radius * radius
area = PI * radius ** 2
print("circle area :", area)

# Python operators
## Arithemtic operators: +, -, *, /, //, %, **
##     % -- gives remainder e.g. 22 % 5 = 2
##     / -- true division e.g. 22 / 5 = 4.4
##    // -- floor division e.g. 22 / 5 = 4 (value after decimal is truncated)
##    ** -- power e.g. 7 ** 3 = 7 * 7 * 7 = 343
## Assignment operators: =, +=, -=, *=, //=, etc.
##    var = value -- right side value assigned to left side var
##    var += value  -->  var = var + value (short-hand or inplace add)
##    var += 1 --> var = var + 1 (No ++ and -- operators like C/Java)
## Comparison operators: <, >, <=, >=, ==, !=
##     Used like condition: Evaluated as bool (True/False)
##     22 > 7 --> True
##     22 < 7 --> False
## Logical operators: and, or, not
##      Used to combine the conditions: Evaluated as bool (True/False)
##      cond1 and cond2 --> True only if both cond are True
##      cond1 or cond2 --> True if any one cond is True
##      not cond --> inverse of cond
## Bitwise operators: Typically used in embedded programming
##      &, |, ~, ^, <<, >>
##      YouTube Tutorial:
## Special operators:
##      is, is not, in, not in
