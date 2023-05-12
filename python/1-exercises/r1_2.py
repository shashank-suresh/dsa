def is_even(k):
    return True if bin(k)[-1] == '0' else False

k = int(input())
print("Even" if is_even(k) else "Odd")