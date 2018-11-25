# Math Symbols ————————————————————————————————————————————————————————————————>
+ plus
- minus
/ slash
* asterik
% percent
< less-than
> greater-than
<= less-than-equal
>= greater-than-equal


# rounds a float number to a whole number.
print round(1.64426)


#The order of calculations used by Python is the same as in the US:
PEMDAS:
1. Parentheses
2. Exponents
3. Multiplication
4. Division
5. Addition
6. Subtraction


# Adding two integers —————————————————————————————————————————————————————————>
def addition(a, b):
    result = 0
    result += a + b
    return result

print addition(5, 10) # 15


# Adding two float numbers ————————————————————————————————————————————————————>
def addition(a, b):
    float(a)
    float(b)
    result = 0
    result += a + b
    return result

print addition(5.5, 10) # 15.5
