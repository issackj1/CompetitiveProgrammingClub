num = input().split()
distance = float(num[0])
hives = int(num[1])
vector = []
sweet = 0
sour = 0

while(distance != 0.0 and hives != 0):
    for i in range(hives):
        coord = input().split()
        x = float(coord[0])
        y = float(coord[1])
        vector.append([x, y])

    for i in range(len(vector)):
        x = vector[i][0]
        y = vector[i][1]
        isSour = False
        for j in range(len(vector)):
            if(j != i):
                if(abs(x - vector[j][0]) <= distance):
                    isSour = True
                    break
                if(abs(y - vector[j][1]) <= distance):
                    isSour = True
                    break
        if(isSour):
            sour += 1
        else:
            sweet += 1
    print("%s sour, %s sweet" % (sour, sweet))
    num = input().split()
    distance = float(num[0])
    hives = int(num[1])
    vector = []
    sweet = 0
    sour = 0
