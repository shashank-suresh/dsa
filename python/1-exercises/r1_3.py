def minmax(data):
    data.sort()
    return data[0], data[-1]

data = list(map(int, input().split()))
print(minmax(data))