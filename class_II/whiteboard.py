my_dict = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}

# Given an object/dictionary with keys and values that consist of both strings and integers, 
# design an algorithm to calculate and return the sum of all of the numeric values.
# Your algorithm should return 41, the sum of the values 23 and 18.
# You may use whatever programming language you'd like.

# need to move through dictionary, check if val is int or float

nums = []
for k,v in my_dict.items():
    if type(v) == int or type(v) == float:
        nums.append(v)
print(sum(nums))
# print(my_dict["cat"])