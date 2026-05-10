arr = [1,2,3,4,6]
n = 6

total = n * (n + 1) // 2
missing = total - sum(arr)

print(missing)