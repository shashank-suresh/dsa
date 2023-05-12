def is_multiple(n, m):
    for i in range(1, m):
        if n == m * i:
            return True
    return False

n, m = map(int, input().split())
print("Yes" if is_multiple(n, m) else "No")