arry1 = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]


"output: 4 + -1 + 9 + -56 + 201 + 18 = 175"



add_all = 0

for i in arry1:
    add_all += min(i)
    print(add_all)

print(add_all)
