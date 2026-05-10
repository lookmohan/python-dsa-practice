arr = [1,2,3,4,5,6]

def even(arr):
    return [i for i in arr if i % 2 == 0]
print(even(arr))