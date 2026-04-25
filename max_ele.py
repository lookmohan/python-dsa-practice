arr = [2,0,29,100,46,7,9,10]

def maxi(arr):
    return max(arr)
print(maxi(arr))

def max_ele(arr):
    largest = arr[0]
    for i in arr:
        if largest < i:
            largest = i
    return largest

print(max_ele(arr))


# ===================== WORKFLOW =====================
# Two approaches to find the maximum element:
#
# Approach 1 - Built-in max() (maxi):
# 1. Directly uses Python's max() function
# 2. Returns the maximum value from the array
#
# Approach 2 - Manual Iteration (max_ele):
# 1. Assume first element is the largest
# 2. Loop through all elements
# 3. If largest < current element -> update largest
# 4. Return largest after loop ends
#
# Example : arr = [2,0,29,100,46,7,9,10] -> Output: 100
# Time Complexity : O(n) | Space Complexity : O(1)
# =====================================================