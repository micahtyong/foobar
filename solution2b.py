def solution(total_lambs):
    if total_lambs <= 1 or total_lambs >= 10**9:
        return 0
    max_hench = pay_minimum(total_lambs)
    min_hench = pay_maximum(total_lambs)
    # print(max_hench, len(max_hench))
    # print(min_hench, len(min_hench))
    return abs(len(max_hench) - len(min_hench))


def pay_minimum(total_lambs):
    total = 2
    payoutList = [1, 1]
    n = 2
    while n <= total_lambs:
        pay = payoutList[n - 1] + payoutList[n - 2]
        payoutList.append(pay)
        total += pay
        if total > total_lambs:
            break
        n += 1
    return payoutList

# Pay Maximum by Doubling


def pay_maximum(total_lambs):
    total = 0
    payoutList = []
    n = 0
    while n <= total_lambs:  # unnecessarily long while loop
        pay = 2 ** n
        payoutList.append(pay)
        total += pay
        if total > total_lambs:
            break
        n += 1
    return payoutList


print(solution(143))
print(solution(10))
