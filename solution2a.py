# Foobar Challenge by Google

def solution(n, b):
    '''
    Given a string n and base b, return the length of the ending cycle specified by the challenge. 
    '''
    return helper(n, b, [])

def helper(n, b, cycle):
    # Step 1: Get digits in sorted order
    digits = list(n)
    digits = list(map(int, digits))
    digits.sort(reverse=True)
    digits = [str(digit) for digit in digits]

    # Step 2: Define x (desc) and y (asc)
    x = "".join(digits)
    y = x[::-1]
    x_int, y_int = int(x, b), int(y, b)

    # Step 3: Define z = x - y
    z = numberToBase(x_int - y_int, b)
    k = len(n)
    while (len(z) < k):
        z.insert(0, '0')

    # Step 4: Recursive call
    if (z in cycle):
        cycle_length = len(cycle) - cycle.index(z)
        return cycle_length
    else:
        cycle.append(z)
        return helper(z, b, cycle)


def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

print(solution('1211', 10))
print(solution('210022', 3))
