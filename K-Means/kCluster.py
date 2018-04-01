import csv
import random
import math
#Changes

COORDINATES = []
CENTROID = []
clusters = []
K = 3
NUM_POINTS = 0
XMIN = 2.9
XMAX = 3.9
YMIN = 0.1
YMAX = 0.4

def readIntoFile(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        minX = minY = 10000
        maxX = maxY = -10000
        for line in reader:
            if (float(line[0]) > maxX):
                XMAX = float(line[0])
                maxX = float(line[0])
            if (float(line[1]) > maxY):
                YMAX = float(line[1])
                maxY = float(line[1])
            if (float(line[0]) < minX):
                XMIN = float(line[0])
                minX = float(line[0])
            if (float(line[1]) < minY):
                YMIN = float(line[1])
                minY = float(line[1])
            COORDINATES.append([float(line[0]),float(line[1])])

    NUM_POINTS = len(COORDINATES)
    for point in COORDINATES:
        print("Points: " + str(point))
    print("max: (" + str(XMAX) + ", " + str(YMAX) + ")")
    print("min: (" + str(XMIN) + ", " + str(YMIN) + ")")

def generateInitialK():
    for center in range(K):
        CENTROID.append([random.uniform(XMIN,XMAX), random.uniform(YMIN,YMAX)])
    for kPoint in CENTROID:
        print("Centroid:"  + str(kPoint))

def euclideanDist(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return math.sqrt(math.pow(x,2) + math.pow(y,2))

def generateClusterArray():
    for i in range(len(CENTROID)):
        clusters.append([])

def assignCluster():
    minDist = []
    generateClusterArray()
    for point in COORDINATES:
        minDist = []
        for i in range(len(CENTROID)):
            minDist.append([float(euclideanDist(CENTROID[i],point)), int(i)])
        minDist.sort(key=lambda pt: pt[0])
        clusters[minDist[0][1]].append(point)
    for cluster in clusters:
        print("Cluster: "+ str(cluster))
    print("length: " + str(len(clusters)))

def clusterAvg():
    sumX = 0
    sumY = 0
    size = 0
    for eachClust in range(K):
        for ptInClust in range(len(clusters[eachClust])):
            size = len(clusters[eachClust])
            sumX += clusters[eachClust][ptInClust][0]
            sumY += clusters[eachClust][ptInClust][1]
        CENTROID.append([sumX/size, sumY/size])
    for center in CENTROID:
        print(center)
    print(len(CENTROID))

def converge():
    readIntoFile("test.csv")
    generateInitialK()
    assignCluster()
    clusterAvg()

    for i in range(len(CENTROID)):
        print("hey")
        for j in range(i+K, len(CENTROID)):
            print("gucci")
            if(CENTROID[i][0] - CENTROID[j][0] > 0 and CENTROID[i][1] - CENTROID[j][1] > 0):
                print("hey lil mama")
                assignCluster()
                clusterAvg()

converge()
