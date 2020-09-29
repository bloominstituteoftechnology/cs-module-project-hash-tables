
"""
Add up and print the sum of all of the minimum elements of each inner
 array:
[[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
The expected output is given by:
4 + -1 + 9 + -56 + 201 + 18 = 175
Verbalize your thought process as much as possible before writing any code.
 Run through the UPER problem solving framework while going
  through your thought process.
  """

arr = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

def minElementSum(array):
    minElements = []
    for innerArr in array:
        element = min(innerArr)
        minElements.append(element)
    return sum(minElements)

print(minElementSum(arr))
    