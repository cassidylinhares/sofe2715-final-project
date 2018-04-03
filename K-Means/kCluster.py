import csv
import random
import math
import plotly.plotly as py
import plotly.graph_objs as go
#plotly to plot graph

COORDINATES = []
CENTROID = []
clusters = []

K = 3

def readIntoFile(filename):     #read csv file and store into coordinates array
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for line in reader:
            #find max and min x and y values to generate initial values
            COORDINATES.append([float(line[0]),float(line[1])]) #COORDINATES[[x,y]]
    for point in COORDINATES:
        print("Points: " + str(point))

def generateInitialK(): #generate N number of centroids using min & max as bounds
    #minX = minY = 10000
    #maxX = maxY = -10000
    XMIN = YMIN = 10000
    XMAX = YMAX = -10000
    for pt in COORDINATES:
        if pt[0] > XMAX:
            XMAX = pt[0]
        if pt[1] > YMAX:
            YMAX = pt[1]
        if pt[0]  < XMIN:
            XMIN = pt[0]
        if pt[1]  < YMIN:
            YMIN = pt[1]
    print("max: (" + str(XMAX) + ", " + str(YMAX) + ")")
    print("min: (" + str(XMIN) + ", " + str(YMIN) + ")")
    for center in range(K):
        CENTROID.append([random.uniform(XMIN,XMAX), random.uniform(YMIN,YMAX)]) #add to centroid array [[x,y]]
    for kPoint in CENTROID:
        print("Centroid:"  + str(kPoint))

def euclideanDist(p1, p2): #calculate distance between 2 given points
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return math.sqrt(math.pow(x,2) + math.pow(y,2)) #using the euclidean distance

def generateClusterArray(): #make an empty array with N number of Clusters
    for i in range(K):
        clusters.append([])

def assignCluster(): #assign each point to the proper cluster
    minDist = []
    generateClusterArray()
    for point in COORDINATES:
        minDist = []
        #goin backwards through centroid array and only going for the # of clusters
        for i in range(len(CENTROID)-1, len(CENTROID)-(1+K),-1):
            #check distance between point with each centroid [[distance, index]]
            minDist.append([float(euclideanDist(CENTROID[i],point)), int(i)])
        minDist.sort(key=lambda pt: pt[0]) #sort by the distance
        clusters[minDist[0][1]].append(point) #put the point with smallest distance in proper cluster
        #clusters[cluster0[[x,y],[x,y]], cluster1[[x,y],[x,y]]]
    print("Cluster length: " + str(len(clusters)))

def clusterAvg(step):
    sumX = 0
    sumY = 0
    size = 1
    print("Step: " + str(step))
    for eachClust in range(step, len(clusters)): #go through the last K clusters
        sumX = 0
        sumY = 0
        for ptInClust in range(len(clusters[eachClust])):
            if(len(clusters[eachClust]) >1):
                sumX += clusters[eachClust][ptInClust][0]
                sumY += clusters[eachClust][ptInClust][1]
                size = len(clusters[eachClust])
            elif(len(clusters[eachClust]) == 1):
                sumX = clusters[eachClust][ptInClust][0]
                sumY = clusters[eachClust][ptInClust][1]
                size = len(clusters[eachClust])
            elif(len(clusters[eachClust]) <= 0) :
                size = len(clusters[eachClust])+1
                sumX = random.uniform(XMIN,XMAX)
                sumY = random.uniform(YMIN,YMAX)
        print("Cluster size: " + str(size) + " sum X: " + str(sumX))
        CENTROID.append([sumX/size, sumY/size]) #calculate avg of points in each cluster
        print("length: " + str(len(clusters)) + " Index: " + str(eachClust))
    for center in CENTROID:
        print(center)

def converge(file, threshHold):
    diffX = 0
    diffY = 0
    step = 0
    shift = []
    readIntoFile(file)
    generateInitialK()
    assignCluster()
    clusterAvg(step)

    for i in range(step, len(CENTROID)): #get differences bewteen first generated centroid and centroid after avg is taken
        for j in range(step):
            diffX = CENTROID[i][0] - CENTROID[j][0]
            diffY = CENTROID[i][1] - CENTROID[j][1]
            shift.append([float(diffX), float(diffY)])
            print("Difference1: " + str(diffX) + ", " + str(diffY))

    i = 0
    #repeat assignment of points to clusters and averaging new centroids if difference between centroids is above acceptable limit
    #or keep repeating until end of shift array. Shift of 0 means that there is no shift in centroids
    while(i <= 15)#len(shift) and (abs(shift[i][0]) > threshHold and abs(shift[i][1]) > threshHold)):
        i +=1
        step += K #to know which clusters to check avg of. Get avg of last K clusters
        assignCluster()
        clusterAvg(step)
        '''
        for i in range(step, len(CENTROID)): #recalculate difference for most recent calculated centroids, and add them to shift array
            for j in range(step):
                diffX = CENTROID[i][0] - CENTROID[j][0]
                diffY = CENTROID[i][1] - CENTROID[j][1]
                shift.append([float(diffX), float(diffY)])
                print("Difference: " + str(diffX) + ", " + str(diffY))'''
    print("Indec " + str(i) + " Diff len: " + str(len(shift)))


def graph(): #plot with plotly
    cluster_plot = []
    k_plot = []
    trace = []
    center_point = []
    colours = ['rgb(0, 0, 255)', 'rgb(0, 128, 0)', 'rgb(255, 0, 0)', 'rgb(0, 255, 255)', 'rgb(255, 191, 0)']

    for pts in range(len(CENTROID)-1, len(CENTROID)-(1+K),-1): #grab the most recent centroids
        k_plot.append(CENTROID[pts])

    for pts in range(len(clusters)-1, len(clusters)-(1+K),-1): #grab most recent cluster
        cluster_plot.append(clusters[pts])

    for ln in range(len(cluster_plot)):
        for pt in range(len(cluster_plot[ln])):
            trace.append(go.Scattergl( #make a trace for each point cluster
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
        center_point.append(go.Scattergl( #make a trace for each centroid
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
    py.iplot(fig, filename= 'clusters') #plot data

file = input("Enter filename: ")
tolerance = input("Enter tolerance level: ")
K_in = input("Enter number of clusters (must be between 2-5): ")
while int(K_in) > 5 or int(K_in) < 2:
    K_in = input("INVALID. Enter number of clusters (must be between 2-5): ")
K = int(K_in)
converge(str(file), float(tolerance))
graph()
