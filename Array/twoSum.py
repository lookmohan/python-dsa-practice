nums = [2,7,11,15]
target = 9
# output : [0,1]
def twoSum(nums,target):
    hashmap = {}
    
    for i in range(len(nums)):
        minus = target - nums[i]
        if minus in hashmap:
            return [hashmap[minus],i]
        hashmap[nums[i]] = i

print(twoSum(nums,target))


# ===================== WORKFLOW =====================
# Uses a hashmap to find two indices whose values sum to target
# 1. Create an empty hashmap {}
# 2. For each element nums[i]:
#    a. Calculate minus = target - nums[i]
#    b. Check if 'minus' already exists in hashmap:
#       - Yes -> found the pair! return [hashmap[minus], i]
#       - No  -> store hashmap[nums[i]] = i and continue
# Trace for nums=[2,7,11,15], target=9:
#   i=0 : minus=7, not in {} -> store {2:0}
#   i=1 : minus=2, 2 in {2:0} -> return [0, 1]
#   Output: [0, 1]
# Time Complexity : O(n) | Space Complexity : O(n)
# =====================================================