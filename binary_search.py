arr = [1,2,3,4,5,6]
target = 4
# output : 3 <- index position
def binarySearch(arr,target):
    left = 0
    right = len(arr)-1
    while left<=right:
        middle = (left+right)//2
        if arr[middle]==target :
            return middle
        elif arr[middle]<target:
            left = middle + 1
        else:
            right = middle -1
    return -1

print(binarySearch(arr,target))  # Time complexity : 0(log n) => Divide & Conquor Technique


# ===================== WORKFLOW =====================
# 1. Start with two pointers: left = 0, right = last index
# 2. Calculate middle index -> middle = (left + right) // 2
# 3. If arr[middle] == target -> return middle (found!)
# 4. If arr[middle] < target  -> move left pointer to middle + 1 (search right half)
# 5. If arr[middle] > target  -> move right pointer to middle - 1 (search left half)
# 6. Repeat steps 2-5 until left > right
# 7. If target not found -> return -1
# Array must be sorted for binary search to work
# Time Complexity : O(log n) | Space Complexity : O(1)
# =====================================================