arr = [1,2,3,4]

def sec_lar(arr):
    lar = arr[0]
    sec_lar = float('inf')

    for i in arr: # 1/2/3/4
        if i > lar:  # 1>1=False / 2>1=True / 3>2=True / 4>3=True
            sec_lar = lar #sec_lar = 1 / sec_lar = 2 / sec_lar = 3
            lar = i       #lar = 2 / lar = 3 / lar = 4
        elif i < lar and i > sec_lar: # 1<1 and 1>inf=False/
            sec_lar = i # inf /

    return sec_lar

print(sec_lar(arr))


# ===================== WORKFLOW =====================
# 1. Initialize lar = arr[0], sec_lar = +infinity
# 2. Loop through each element i:
#    - If i > lar:
#        sec_lar = lar  (old largest becomes second largest)
#        lar = i        (update new largest)
#    - Elif i < lar and i > sec_lar:
#        sec_lar = i    (update second largest)
# 3. Return sec_lar
# Trace for arr = [1, 2, 3, 4]:
#   i=1 : lar=1,  sec=inf
#   i=2 : 2>1 -> sec=1, lar=2
#   i=3 : 3>2 -> sec=2, lar=3
#   i=4 : 4>3 -> sec=3, lar=4
#   Output: 3
# Time Complexity : O(n) | Space Complexity : O(1)
# =====================================================
