# resize an array :

arr = [1, 2, 3]
new_size = 20
new_arr = [0] * new_size

for i in range(len(arr)):
    new_arr[i] = arr[i]

print(new_arr,len(new_arr))