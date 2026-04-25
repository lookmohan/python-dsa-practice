
arr = [0,2,83,1,939,622,1,3,42,8]

def largest(arr):
    lar = arr[0]
    for i in arr:
        if i > lar:
            lar = i
    return lar
        
print(largest(arr))


arr1 = [1,2,3,45,576]
def sorted_lar_ele(arr1):
    sort = sorted(arr1)
    large = sort[-1]
    return large

print(sorted_lar_ele(arr1))


# ===================== WORKFLOW =====================
# Two approaches to find the largest element:
#
# Approach 1 - Manual Iteration (largest):
# 1. Assume first element is the largest
# 2. Loop through each element in arr
# 3. If current element > lar, update lar
# 4. Return lar after full loop
#
# Approach 2 - Using sorted() (sorted_lar_ele):
# 1. Sort the array in ascending order
# 2. The last element sort[-1] is the largest
# 3. Return it
#
# Example : arr = [0,2,83,1,939,622,1,3,42,8] -> Output: 939
# Time Complexity : O(n) for Approach 1 | O(n log n) for Approach 2
# =====================================================
