# x = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# minTotal = 0

# for i in x:
#     curMin = i[0]
#     for y in i:
#         if y < curMin:
#             curMin = y
#     minTotal += curMin

# print(minTotal)

y = [
    [8, [4]],
    [[90, 91], -1, 3],
    [9, 62],
    [[-7, -1, [-56, [-6]]]],
    [201],
    [[76, 0], 18],
]


def minTotal(arr):
    minSum = 0
    iterator = 0
    curMin = arr[iterator]
    for i in arr:
        iterator += 1
        if isinstance(i, list):
            curMin = arr[iterator]
            minSum += minTotal(i)
        else:
            minSum += min(i)
    return minSum


print(minTotal(y))
