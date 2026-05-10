arr = [0,1,2,3,0,4,5]

# output : 1,2,3,4,5,0,0
new = []
zero = []
for i in arr :
    if i != 0 :
        new.append(i)
    elif i == 0 :
        zero.append(i)
print(new+zero)