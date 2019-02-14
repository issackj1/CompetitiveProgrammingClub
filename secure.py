num = int(input())
building = set()
one = []

for i in range(num):
    theLog = input()
    one = theLog.split(" ")
    if one[0] == "entry":
        if(one[1] in building):
            print(one[1] + " entered" + " (ANOMALY)")
        else:
            print(one[1] + " entered")
            building.add(one[1])
    elif one[0] == "exit":
        if(one[1] in building):
            print(one[1] + " exited")
            building.remove(one[1])
        else:
            print(one[1] + " exited " + "(ANOMALY)")
