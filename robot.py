num = list(map(int, input().split()))
width = num[0]
length = num[1]
xcoord = 0
ycoord = 0
thinksx = 0
thinksy = 0

while(num[0] != 0 and num[1] != 0):
    segments = int(input())
    maxdown = num[1]
    maxright = num[0]
    for i in range(segments):
        movement = input().split()
        direction = movement[0]
        meters = int(movement[1])
        if(direction == "u"):
            thinksy = thinksy + meters
            if(ycoord + meters >= maxdown):
                ycoord = maxdown - 1
            else:
                ycoord = ycoord + meters
        elif (direction == "d"):
            thinksy = thinksy - meters
            if(ycoord - meters < 0):
                ycoord = 0
            else:
                ycoord = ycoord - meters
        elif( direction == "l"):
            thinksx = thinksx - meters
            if(xcoord - meters < 0):
                xcoord = 0
            else:
                xcoord = xcoord - meters
        else:
            thinksx = thinksx + meters
            if(xcoord + meters >= maxright):
                xcoord = maxright - 1
            else:
                xcoord = xcoord + meters
    print("Robot thinks %d %d" %(thinksx, thinksy))
    print("Actually at %d %d" % (xcoord, ycoord))
    num = list(map(int, input().split()))
    width = num[0]
    length = num[1]
    xcoord = 0
    ycoord = 0
    thinksx = 0
    thinksy = 0