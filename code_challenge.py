'''
Add up and print the sum of the all of the minimum elements of each inner array:
```
[[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
```
The expected output is given by:
```
4 + -1 + 9 + -56 + 201 + 18 = 175
```
'''



arr = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

length = len(arr)

lowestArr = [0] * length

index = 0
for i in arr:
    lowestArr[index] = i[0]
    for j in i:
        if j < lowestArr[index]:
            lowestArr[index] = j
    index += 1

print(sum(lowestArr))