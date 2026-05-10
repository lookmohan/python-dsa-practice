arr = [1,2,3,4,5]

def left_rotate(arr):
    temp = arr[0]
    for i in range(1,len(arr)):
        arr[i-1] = arr[i]
    arr[len(arr)-1] = temp
    return arr

print(left_rotate(arr))


# ===================== WORKFLOW =====================
# 1. Save the first element in temp (temp = arr[0])
# 2. Shift every element one position to the left:
#    arr[i-1] = arr[i] for i in range(1, len(arr))
# 3. Place the saved temp at the last position
# 4. Return the modified array
# Example:
#   Input  : [1, 2, 3, 4, 5]
#   Step 1 : temp = 1
#   Step 2 : [2, 3, 4, 5, 5]
#   Step 3 : [2, 3, 4, 5, 1]
#   Output : [2, 3, 4, 5, 1]
# Time Complexity : O(n) | Space Complexity : O(1)
# =====================================================