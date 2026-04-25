arr1 = [1,2,3,4,5]
arr2 = [6,7,8,9,10]

def mergeArray(arr1,arr2):
    print('simple concatination method')
    return arr1 + arr2

def mergeSrotedArray(arr1,arr2):
    print('Two pointer method')
    
    i = 0
    j = 0
    merge = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merge.append(arr1[i])
            i+=1
        else:
            merge.append(arr2[j])
            j+=1
        
    while i < len(arr1):
        merge.append(arr1[i])
        i+=1

    while j < len(arr2):
        merge.append(arr2[j])
        j+=1
    
    return merge



print(mergeArray(arr1,arr2))
print(mergeSrotedArray(arr1,arr2))


# ===================== WORKFLOW =====================
# Two approaches to merge two sorted arrays:
#
# Approach 1 - Simple Concatenation (mergeArray):
# 1. Use + operator to combine arr1 and arr2
# 2. Returns a new merged list (order not guaranteed if inputs unsorted)
#
# Approach 2 - Two Pointer Method (mergeSrotedArray):
# 1. Use two pointers i=0 (arr1) and j=0 (arr2)
# 2. Compare arr1[i] and arr2[j]:
#    - Smaller element gets appended to merge list
#    - That pointer advances by 1
# 3. After one array is exhausted, append remaining elements of the other
# 4. Return the merged sorted list
#
# Example:
#   arr1=[1,2,3,4,5] arr2=[6,7,8,9,10]
#   Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Time Complexity : O(n+m) | Space Complexity : O(n+m)
# =====================================================
