#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

a = input('Enter value of "a": ')
a2 = int(a)

b = input('Enter value of "b": ')
b2 = int(b)

c = input('Enter value of "c": ')
c2 = int(c)

x = ((c2 - b2)/a2)
result = str(x)

print('x = ' + result)


