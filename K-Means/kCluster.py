import csv
import random
import math
import plotly.plotly as py
import plotly.graph_objs as go
#Changes

COORDINATES = []
CENTROID = []
clusters = []
K = 3
NUM_POINTS = 0
XMIN = 1.5
XMAX = 4.1
YMIN = 0.1
YMAX = 2.3

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
    for i in range(K):
        clusters.append([])

def assignCluster():
    minDist = []
    generateClusterArray()
    for point in COORDINATES:
        minDist = []
        for i in range(len(CENTROID)-1, len(CENTROID)-(1+K),-1):
            minDist.append([float(euclideanDist(CENTROID[i],point)), int(i)])
        minDist.sort(key=lambda pt: pt[0])
        clusters[minDist[0][1]].append(point)
    for cluster in clusters:
        print("Cluster: "+ str(cluster))
    print("length: " + str(len(clusters)))


def clusterAvg(step):
    sumX = 0
    sumY = 0
    size = 0
    print("Step: " + str(step))
    for eachClust in range(step, len(clusters)):
        sumX = 0
        sumY = 0
        for ptInClust in range(len(clusters[eachClust])):
            size = len(clusters[eachClust])

            if(size>1):
                sumX += clusters[eachClust][ptInClust][0]
                sumY += clusters[eachClust][ptInClust][1]
            elif(size == 1):
                sumX = clusters[eachClust][ptInClust][0]
                sumY = clusters[eachClust][ptInClust][1]
            elif(size == 0) :
                sumX = random.uniform(XMIN,XMAX)
                sumY = random.uniform(YMIN,YMAX)
                size = 1
        print("Cluster size: " + str(size) + " sum X: " + str(sumX))
        CENTROID.append([sumX/size, sumY/size])
        print("length: " + str(len(clusters)) + " Index: " + str(eachClust))
    for center in CENTROID:
        print(center)

def converge():
    diffX = 0
    diffY = 0
    step = 0
    shift = []
    readIntoFile("exercise-1.csv")
    generateInitialK()
    assignCluster()
    clusterAvg(step)

    for i in range(len(CENTROID)):
        for j in range(i+K, len(CENTROID)):
            diffX = CENTROID[i][0] - CENTROID[j][0]
            diffY = CENTROID[i][1] - CENTROID[j][1]
            shift.append([float(diffX), float(diffY)])
            print("Difference: " + str(diffX) + ", " + str(diffY))

    i = 0

    while(i < len(shift) and (abs(shift[i][0]) > 0.02 and abs(shift[i][1]) > 0.02)):
        i +=1
        step += K
        assignCluster()
        clusterAvg(step)
    print("Indec " + str(i) + " Diff len: " + str(len(shift)))


def graph():
    cluster_plot = []
    k_plot = []
    trace = []
    center_point = []
    colours = ['rgb(0, 0, 255)', 'rgb(0, 128, 0)', 'rgb(255, 0, 0)', 'rgb(0, 255, 255)', 'rgb(255, 191, 0)']

    for pts in range(len(CENTROID)-1, len(CENTROID)-(1+K),-1):
        k_plot.append(CENTROID[pts])

    for pts in range(len(clusters)-1, len(clusters)-(1+K),-1):
        cluster_plot.append(clusters[pts])

    for ln in range(len(cluster_plot)):
        for pt in range(len(cluster_plot[ln])):
            trace.append(go.Scatter(
                x = cluster_plot[ln][pt][0],
                y = cluster_plot[ln][pt][1],
                name = 'Cluster ' + str(ln+1),
                mode = 'markers',
                marker = dict(
                    size = 7,
                    color = colours[ln],
                    line = dict(
                        width = 2,
                        color = 'rgb(102, 102, 102)'
                    )
                )
            ))
        center_point.append(go.Scatter(
            x = k_plot[ln][0],
            y = k_plot[ln][1],
            name = 'Centroid ' + str(ln+1),
            mode = 'markers',
            marker = dict(
                size = 12,
                color = 'rgb(0, 0, 0)',
                line = dict(
                    width = 2,
                )
            )
        ))
    data = []
    for i in trace:
        data.append(i)
    for i in center_point:
        data.append(i)
    layout = dict(title= 'Clusters', yaxis = dict(zeroline = False), xaxis = dict(zeroline = False))
    fig = dict(data = data, layout = layout)
    py.iplot(fig, filename= 'clusters')


converge()
graph()
