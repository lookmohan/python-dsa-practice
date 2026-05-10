arr = [1,23,46,2]
ar = [1,2,3,4,5]

def is_Sorted(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True
            
print(is_Sorted(arr))
print(is_Sorted(ar))


# ===================== WORKFLOW =====================
# 1. Loop from index 1 to len(arr)-1
# 2. Compare each element with the previous one:
#    - If arr[i] < arr[i-1] -> array is NOT sorted -> return False
# 3. If loop completes without returning False -> return True
# Example:
#   arr  = [1, 23, 46, 2] -> at i=3: 2 < 46 -> return False
#   ar   = [1, 2, 3, 4, 5] -> all elements ascending -> return True
# Time Complexity : O(n) | Space Complexity : O(1)
# =====================================================
