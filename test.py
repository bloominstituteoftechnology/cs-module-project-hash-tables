def getsum(dict):
    total = 0 
    for i in dict:
        if type(dict[i]) == int:
            total += dict[i]
    return total

test = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}
print(getsum(test))