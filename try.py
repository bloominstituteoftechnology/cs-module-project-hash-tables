# This is the file that I use to just try stuff

a = 4
b = 5
z = 3

z %= (a+b)*10

print(z)

first = "poker."
second = 'the pokers"'
theTuple = (".", "\"")

print(f"first is {first.endswith(theTuple)}")
print(f"second is  {second.endswith(theTuple)}")




theList = [1,2,3,4]

def myPerm(theList):
    outPut = []
    if len(theList) == 1:
        return theList
  
    for i in range(len(theList)):
        # doing the swapping of the 
        # value that was chosen
        
        # will now do the recursive call to the permutaton function
        
        outPut += [theList[i]] + myPerm(theList[:i] + theList[i+1:])
    return outPut


print(myPerm(theList))


