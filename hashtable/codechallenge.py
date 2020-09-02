data = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

def getSumMin(arr):
    sum = 0
    for i in arr:
        min = i[0]
        for x in i:
            if min > x:
                min = x
        sum += min
    return sum
    

print(getSumMin(data))