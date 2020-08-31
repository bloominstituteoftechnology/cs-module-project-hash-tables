
array = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]



def sumofMin(array):
    sum =  0
    for i in array:
        sum += min(i)
    return sum


print(sumofMin(array))
    



        

