# Find the Access Codes


def solution(l):
    # Your answer here
    return solution_faster(l)


def solution_faster(l):
    access_codes = [0 for elem in l]
    num_codes = 0
    for i in range(len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                access_codes[i] += 1
                num_codes += access_codes[j]
    return num_codes

# This soln runs too slow, about O(n^3) time.


def solution_naive(l):
    if (l is None):
        return 0
    l.sort()
    access_codes = []
    for i in range(len(l)):
        access_codes_starting_with_i = []
        triple(l[i + 1:], l[i], [l[i]], access_codes_starting_with_i)
        access_codes.extend(access_codes_starting_with_i)
    return len(access_codes)


def triple(l, elem, lst, access_codes):
    if len(lst) == 3:
        access_codes.append(lst)
    else:
        for i in range(len(l)):
            next_elem = l[i]
            if next_elem % elem == 0:
                new_lst = lst[:]
                new_lst.append(next_elem)
                triple(l[i + 1:], next_elem, new_lst, access_codes)


# lst = []
# triple([2, 3, 4, 5, 6], 1, [1], lst)
# print(lst)

print(solution([1, 2, 3, 4, 5, 6]))

print(solution([1, 1, 1]))

# find_triple([1, 2, 3, 4, 5, 6])
# Expect
# [
#     [1, 2, 4],
#     [1, 2, 6],
#     [1, 3, 6]
# ]


# solution([1, 2, 3, 4, 5, 6])  # 3
# 1 2 4
# 1 2 6
# 1 3 6
# solution([1, 1, 1])  # 1

# Iterative
# def find_triple(l):
#     if len(l) < 3:
#         return 0
#     triple = [l[0]]
#     elem = triple[0]
#     for i in range(1, len(l)):
#         if l[i] % elem == 0:
#             triple.append(l[i])
#             elem = l[i]
#         if len(triple) == 3:
#             break
#     print(triple)
#     return triple
