from math import sqrt, log, ceil, floor, pow
import math


def solution(n):
    '''
    Input: String n
    Output: Minimum number of "steps" to reach 1.
    '''
    n = int(n)
    return solution_f(n)

# Same as e but with iteration


def solution_f(n):
    num_steps = 0
    while (n > 1):
        # Most significant digit is 0
        if (n % 2 == 0):
            n = n // 2
        # n == 3 or two last significant digits are 01
        elif (n == 3 or n % 4 == 1):
            n = n - 1
        else:
            n = n + 1
        num_steps += 1
    return num_steps


def solution_e(n):
    # Base case
    if (n == 1):
        return 0
    # Most significant digit is 0
    elif (n % 2 == 0):
        new_n = n // 2
    # n == 3 or two last significant digits are 01
    elif (n == 3 or n % 4 == 1):
        new_n = n - 1
    else:
        new_n = n + 1

    return 1 + solution_e(new_n)


def solution_d(n):
    num = float(int(n))
    if (num == 1):
        return str(0)

    if (num % 2 == 0):
        new_n = str(int(num / 2))
    elif (((num - 1) / 2) % 2 == 0):
        new_n = str(int(num - 1))
    else:
        new_n = str(int(num + 1))

    return str(1 + int(solution_d(new_n)))


def solution_c(n):
    num = float(int(n))
    if (num == 1):
        return str(0)

    closest_pow_exponent = closest_power(num)
    nearest_pow = math.pow(2, closest_pow_exponent)

    if (num % 2 == 0):
        new_n = str(int(num / 2))
    elif (nearest_pow > num):
        new_n = str(int(num + 1))
    else:
        new_n = str(int(num - 1))

    return str(1 + int(solution_c(new_n)))


def solution_b(n):
    num = float(int(n))
    if (num == 1):
        return str(0)

    sq_num = sqrt(num)
    closest_pow_exponent = closest_power(num)
    nearest_pow = math.pow(2, closest_pow_exponent)

    if (sq_num.is_integer()):
        return str(int(closest_pow_exponent))
    return str(int(closest_pow_exponent + abs(nearest_pow - num)))


def solution_a(n):
    num = float(int(n))
    if (num == 1):
        return str(0)

    closest_pow_exponent = closest_power(num)
    nearest_pow = math.pow(2, closest_pow_exponent)

    if (abs(nearest_pow - num) == 0):
        return str(int(closest_pow_exponent))
    elif (nearest_pow > num):
        new_n = str(int(num + 1))
    else:
        new_n = str(int(num - 1))

    return str(1 + int(solution(new_n)))


def closest_power(x):
    possible_results = floor(log(x, 2)), ceil(log(x, 2))
    return min(possible_results, key=lambda z: abs(x-2**z))


print(solution('44'))
print(solution('32'))
print(solution('33'))
# print(solution('17'))
# print(solution('4'))
