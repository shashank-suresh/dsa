def insertion_sort(arr):
    for i in range(1, len(arr)):
        curr = arr[i]
        j = i

        while j > 0 and arr[j-1] > curr:
            arr[j] = arr[j-1]
            j -= 1
        
        arr[j] = curr

arr = [2, 5, 4, 3, 1, 6]
insertion_sort(arr)
print(arr)