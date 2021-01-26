# The purpose of this kata is to write a program that can do some algebra.
# Write a function expand that takes in an expresion with a single, one character variable,
# and expands it. The expresion is in the form (ax+b)^n where a and b are integers which may be positive or negative,
# x is any one character long variable, and n is a natural number. If a = 1,
# no coeficient will be placed in front of the variable. If a = -1, a "-" will be placed in front of the variable.
#
# The expanded form should be returned as a string in the form ax^b+cx^d+ex^f...
#
# Example:
# expand("(x+1)^2")      # returns "x^2+2x+1"
# expand("(p-1)^3")      # returns "p^3-3p^2+3p-1"
# expand("(2f+4)^6")     # returns "64f^6+768f^5+3840f^4+10240f^3+15360f^2+12288f+4096"
# expand("(-2a-4)^0")    # returns "1"


import re

def factorial(n):
    f = 1
    for i in range(2, n+1):
        f *= i
    return f

def full_val(arg):
    if arg =='':
        return 1
    elif arg == '-':
        return -1
    elif arg == '+':
        return 1
    else:
        return arg

def expand(expr):
    bracket, power = re.split('\^', expr)
    power = int(power)
    bracket = bracket.replace("(", "").replace(")", '')
    if power == 0:
        return '1'
    elif power ==1:
        return bracket

    second = re.findall('([^+-]+$)', bracket)
    second = second[0]
    bracket = bracket.rstrip(second)
    second = bracket[-1] + second
    first = bracket[:-1]
    coeffs = [first, second]
    x = 0; a = 0
    for c in coeffs:
        if re.search('[a-zA-Z]', c):
            x = c
            variable = x[-1]
            x = x[:-1]
        else:
            a = c
    a = int(full_val(a))
    x = int(full_val(x))
    formula = []

    # nCr = (n!) / ((n - r)! * (r)!)

    # n!
    fact = factorial(power)

    # nCr
    for i in range(0, power+1):
        ni_fact = factorial(power-i)
        i_fact = factorial(i)

        a_pow = a ** (power-i)
        x_pow = x ** i
        formula.append(int((fact * a_pow * x_pow) /
                  (ni_fact * i_fact)))

    expanded = ''
    for num, val in enumerate(formula, start=0):
        if num == 0:
            expanded = str(val)
        elif num == 1:
            if val ==1:
                if expanded[0] == '-':
                    expanded = variable + expanded
                else:
                    expanded = variable + '+' + expanded
            elif val == -1:
                if expanded[0] == '-':
                    expanded = '-' + variable + expanded
                else:
                    expanded = '-' + variable + '+' + expanded
            else:
                if expanded[0] == '-':
                    expanded = str(val)+ variable + expanded
                else:
                    expanded = str(val) + variable + '+' +expanded
        else:
            if val ==1:
                if expanded[0] == '-':
                    expanded = variable + '^' + str(num) + expanded
                else:
                    expanded = variable + '^' + str(num) + '+' + expanded
            elif val == -1:
                if expanded[0] == '-':
                    expanded = '-' + variable + '^' + str(num) + expanded
                else:
                    expanded = '-' + variable + '^' + str(num) + '+' + expanded

            else:
                if expanded[0] == '-':
                    expanded = str(val) + variable + '^' + str(num) + expanded
                else:
                    expanded = str(val) + variable + '^' + str(num) + '+' + expanded
    return expanded




print(expand("(x+1)^3"))

