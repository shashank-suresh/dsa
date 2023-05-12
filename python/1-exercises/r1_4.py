def sq_sum_less_than(n):
    sum_ = 0
    for i in range(1, n):
        sum_ += i**2

    return sum_

print(sq_sum_less_than(int(input())))