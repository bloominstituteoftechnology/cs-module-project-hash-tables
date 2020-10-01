code = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]


def coding(code):
    minSum = 0
    for n in code:
        minSum += min(n)
    return(minSum)

print(coding(code))
