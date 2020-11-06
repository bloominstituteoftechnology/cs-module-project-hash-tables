# Your code here

theFile = open("robin.txt", "r")
for line in theFile.readlines():
    print(line)
theFile.close()