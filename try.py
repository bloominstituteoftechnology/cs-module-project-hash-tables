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

def mySwap(theList, left, right):
    temp = theList[left]
    theList[left] = theList[right]
    theList[right] = temp
    return theList


theList = [1,2,3]

def myPerm(theList, left, right):
    outPut = []
    if left == right:
        return theList
  
    for i in range(left, right):
        # doing the swap
        breakpoint()
        swappedList = mySwap(theList, left, i)
        # then calling the permutation again
        outPut += myPerm(swappedList, left+1, right)

        
        
    return outPut


print(myPerm(theList, 0, len(theList))-1)


