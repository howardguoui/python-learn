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


class Solution2:
    """
    @param n: An integer
    @return: A list of strings.
    """

    def fizzBuzz(self, n):
        # write your code here
        results = [];
        for i in range(1, n + 1):
            if (i % 3 == 0 and i % 5 == 0):
                results.append("fizz buzz")
            elif (i % 3 == 0):
                results.append("fizz")
            elif (i % 5 == 0):
                results.append("buzz")
            else:
                results.append(str(i))
        return results

    def fizzBuzz2(self, n):
        return ['fizz' * (not i % 3) + ' ' * (not i % 15) + 'buzz' * (not i % 5) or str(i) for i in range(1, n + 1)]


class Solution3:
    """
    @param: n: An integer
    @return: A list of strings.
    """

    def fizzBuzz(self, n):
        # write your code here
        return [' '.join([w + 'zz' for m, w in {3: 'fi', 5: 'bu'}.items() if x % m < 1]) or str(x) for x in
                range(1, n + 1)]
