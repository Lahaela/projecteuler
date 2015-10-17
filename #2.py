total = 0
x = 1
y = 2
while y < 4000000 and x < 4000000:
    x = x + y
    y = x + y
    if x % 2 == 0:
        total = total + x
    elif y % 2 == 0:
        total = total + y
print total + 2

total = 0
x = 1
y = 2
Fibonacci = []
while y < 4000000 and x < 4000000:
    x = x + y
    y = x + y
    Fibonacci.append(x)
    Fibonacci.append(y)
for a in Fibonacci:
    if a % 2 == 0:
        total = total + a

# Generate all Fibonacci numbers
    # Generate the first number, 1
    # Generate the second number
    # First number + second number = third number
    # Second number + third number = fourth number
    # Repeat
# Stop at 4,000,000
# Take all even numbers (Numbers divisible by 2, or #s % 2 == 0)
# add them up
# ==> Result

