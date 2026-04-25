arr = [1,2,3,4,5]
def reverse(arr):
    return arr[::-1]
print(reverse(arr))


# ===================== WORKFLOW =====================
# 1. Use Python slicing with step -1 -> arr[::-1]
#    This creates a new reversed copy of the array
# 2. Return the reversed array
# Example:
#   Input  : [1, 2, 3, 4, 5]
#   Output : [5, 4, 3, 2, 1]
# Note: Does NOT modify the original array
# Time Complexity : O(n) | Space Complexity : O(n)
# =====================================================