# Load Factor

**load factor** = number of elements stored in hash table / number of slots

4 / 8 = 0.5
8 / 8 = 1.0
16 / 8 = 2.0

**How to know when to re-size?**

- If `load factor > 0.7`, grow the table
- If `load factor < 0.2`, shrink the table (down to some minimum)

Grow the table -> double in size
Shrink the table -> halve in size

```py
# When you PUT:
#     if `load_factor` > 0.7:
#         create new arr with double the size of old one
#         for each elem in old arr:
#             PUT in the new arr
```