import csv
import random
#Changes

COORDINATES = []
CENTROID = []
clusters = []
K = 0
NUM_POINTS = 0
xMin = 100000
xMax = -100000
yMin = 100000
yMax = -100000
def readIntoFile(filename):

    with open(filename, "r") as f:
        reader = csv.reader(f)
        minX = minY = 1000
        maxX = maxY = 0
        for line in reader:
            if (float(line[0]) > maxX):
                xMax = float(line[0])
                maxX = float(line[0])
            if (float(line[1]) > maxY):
                yMax = float(line[1])
                maxY = float(line[1])
            if (float(line[0]) > minX):
                xMin = float(line[0])
                minX = float(line[0])
            if (float(line[1]) < minY):
                yMin = float(line[1])
                minY = float(line[1])
            COORDINATES.append([float(line[0]),float(line[1])])

    NUM_POINTS = len(COORDINATES)
    for point in COORDINATES:
        print(point)
    print("max: (" + str(xMax) + ", " + str(yMax) + ")")
    print("min: (" + minX + ", " + minY + ")")

def generateInitialK():
    for center in range(K):
        CENTROID.append([random.uniform(xMin,xMax), random.uniform(yMin,yMax)])

def euclideanDist(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return sqrt(pow(x,2) + pow(y,2))

def generateClusterArray():
    for i in range(len(CENTROID)):
        clusters.append([])

def assignCluster():
    minDist = []
    generateClusterArray()
    for point in COORDINATES:
        minDist = []
        for i in range(len(CENTROID)):
            minDist.append([euclideanDist(CENTROID[i],point), i])
        minDist.sort(key=lambda pt: pt[0])
        clusters[minDist[0][1]].append(point)




readIntoFile("exercise-1.csv")
