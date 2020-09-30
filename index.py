records = [
    ("Tim", "Austin"),
  (  "j", "Redmond"),
    ("paul", "LA"),
    ("Ryan", "Austin"),
    ("TUCKER", "Asheville"),

]

d = {}

for r in records:
   city = r[1]
   name = r[0]
   if city in d:
     d[city].add(name)
   else:
     d[city]= set()
     d[city].add(name)
print(d["Austin"])
print(d["Asheville"])
print(d["LA"])

#Checking for member in dict: 0(1)   
#get: 0(1)


