# coding=utf-8

num = 10
num += 2

print(3 + 2, 4 - 6, 2 * 7)
print(7 / 4, 10 // 4, 7 % 4)

# ------------------------------------------------------------------------------
int_num = 123
digit_1 = int_num % 10
digit_2 = int_num // 10 % 10
digit_3 = int_num // 100
reverse_num = digit_1 * 100 + digit_2 * 10 + digit_3

print(reverse_num)

# ------------------------------------------------------------------------------
float_num = 3.4
print(float_num + 2, float_num * 3.1, float_num / 3, float_num / 1)

num = int(float_num)
float_num = float(num)

# ------------------------------------------------------------------------------
bool_true = True
bool_false = False

year = 2018
is_leap_year = year % 400 == 0 or year % 100 != 0 and year % 4 == 0

# ------------------------------------------------------------------------------
num1 = 10
num2 = 15

temp = num1
num1 = num2
num2 = temp

num1, num2 = num2, num1

class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """

    def fizzBuzz(self, n):
        rst = []
        for i in range(1, n + 1):
            print(i)

            rst.append(str(i))

        for i in range(2, n, 3):
            rst[i] = "fizz"
        for i in range(4, n, 5):
            if rst[i] == "fizz":
                rst[i] = "fizz buzz"
                continue
            rst[i] = "buzz"
        return rst