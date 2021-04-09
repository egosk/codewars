# Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the
# number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print
# “FizzBuzz”.

# def fizz_buzz(n):
#     for i in range(1, n+1):
#         if i%15==0:
#             print("FizzBuzz")
#         elif i%3==0:
#             print("Fizz")
#         elif i%5==0:
#             print("Buzz")
#         else:
#             print(i)

# def fizz_buzz(n):
#     for i in range(1, n+1):
#         tmp = ''
#         if i%3 == 0:
#             tmp += 'Fizz'
#         if i%5 == 0:
#             tmp += 'Buzz'
#         if tmp == '':
#             tmp = i
#         print(tmp)

def fizz_buzz(n):
    def f_b(num):
        condition_1 = (num % 3 == 0)
        condition_2 = (num % 5 == 0)
        if (condition_1 or condition_2):
            return (condition_1 * 'Fizz') + (condition_2*'Buzz')
        return str(num)

    print('\n'.join(f_b(i) for i in range (1, n+1)))


fizz_buzz(100)