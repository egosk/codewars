# TASK:
# Given two numbers: 'left' and 'right' (1 <= 'left' <= 'right' <= 200000000000000) return sum of all '1'
# occurencies in binary representations of numbers between 'left' and 'right' (including both)
# Example:
# countOnes 4 7 should return 8, because:
# 4(dec) = 100(bin), which adds 1 to the result.
# 5(dec) = 101(bin), which adds 2 to the result.
# 6(dec) = 110(bin), which adds 2 to the result.
# 7(dec) = 111(bin), which adds 3 to the result.
# So finally result equals 8.

# TO DO: simple_count function should be updated to run faster

import math

def countOnes(left, right):
    # find smallest x, where x>left, x = 2^n
    # 2^n > left => n>log2(5)
    n = math.ceil(math.log(left, 2))
    x = 2 ** n # n = p1, m = p2

    # find largest y, where y < right, y = 2^m
    m = math.floor(math.log(right, 2))
    y = 2 ** m

    # count ones between x i y == > f(m)- f(n)
    count = f(m) - f(n)

    # count ones between left and x, right and y
    for i in range(left, x):
        count += simple_count(i)

    for j in range(y, right+1):
        count += simple_count(j)


    print(count)
    return count


# f(n) is sum of ones up to (2^n)-1
# f(n) = n*2^(n-1)
def f(n):
    return n * 2 ** (n-1)

def simple_count(num):
    return bin(num).count('1')


countOnes(12,29)