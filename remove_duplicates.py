arr = [1,6,90,11,2,2,3,3,4,5]

def remove_duplicate(arr):
    seen = set()
    res = []
    for i in arr:
        if i not in seen:
            res.append(i)
            seen.add(i)
    return seen,res

print(remove_duplicate(arr))


# ===================== WORKFLOW =====================
# 1. Create an empty set 'seen' and an empty list 'res'
# 2. Loop through each element in arr:
#    - If element is NOT in seen -> append to res, add to seen
#    - If element IS in seen     -> skip it (duplicate)
# 3. Return both seen (set of unique values) and res (ordered unique list)
# Example:
#   Input  : [1, 6, 90, 11, 2, 2, 3, 3, 4, 5]
#   Output : ({1,2,3,4,5,6,11,90}, [1,6,90,11,2,3,4,5])
#   set -> unordered unique values
#   res -> insertion-order unique values
# Time Complexity : O(n) | Space Complexity : O(n)
# =====================================================