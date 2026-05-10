arr = [3, 5, 1, 4, 2]

first = second = float('inf')

for num in arr:
    if num < first:
        second = first
        first = num
    elif num < second and num != first:
        second = num

print(second)