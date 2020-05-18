def solution(total_lambs):
    if total_lambs is None:
        return None
    if total_lambs <= 1 or total_lambs >= 10**9:
        return 0
    max_hench = pay_minimum(total_lambs)
    min_hench = pay_maximum(total_lambs)
    return max_hench - min_hench


def pay_minimum(total_lambs):
    mem_fib = memoize(fib)
    number_of_henchmen = 0
    total = 0
    n = 1
    while (total + mem_fib(n)) <= total_lambs:
        total += mem_fib(n)
        n += 1
        number_of_henchmen += 1
    return number_of_henchmen

# Pay Maximum by Doubling


def pay_maximum(total_lambs):
    total = 0
    n = 1
    henchmen = 0
    while (total + n) <= total_lambs:
        total += n
        n *= 2
        henchmen += 1

    leftover = total_lambs - total
    min_req = (n // 2) + (n // 4)
    while leftover > min_req:
        henchmen += 1
        leftover -= min_req
        min_req = min_req + (n // 2)
    return henchmen

# Helpers


def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n - 1) + fib(n - 2))


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

