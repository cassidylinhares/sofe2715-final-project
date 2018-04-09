import csv
import random
import math
import pygame
import time


#starting state for window
running = True
#window size
win = {"width": 800, "height": 800}

#global variables
COORDINATES = []
CENTROID = []
clusters = []

K = 3

XMIN = 10000
YMIN = 10000
XMAX = -10000
YMAX = -10000

def readIntoFile(filename):  # read csv file and store into coordinates array
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for line in reader:
            #find max and min x and y values to generate initial values
            COORDINATES.append([float(line[0]),float(line[1])]) #COORDINATES[[x,y]]

def generateInitialK(): # generate N number of centroids using min & max as bounds
    global XMIN, XMAX, YMIN, YMAX
    for pt in COORDINATES: #find max and min
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
        print("Initial Centroid:"  + str(kPoint))

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
        # clusters[# of centroids/cluster][# pts in cluster][x,y]

def clusterAvg(step):
    sumX = 0
    sumY = 0
    size = 1
    print("Step: " + str(step))
    for eachClust in range(step, len(clusters)): #go through the last K clusters
        sumX = 0
        sumY = 0
        for ptInClust in range(len(clusters[eachClust])):
            if(len(clusters[eachClust]) >1): #summation of pts in cluster
                sumX += clusters[eachClust][ptInClust][0]
                sumY += clusters[eachClust][ptInClust][1]
                size = len(clusters[eachClust])
            elif(len(clusters[eachClust]) == 1): # if one pt in cluster
                sumX = clusters[eachClust][ptInClust][0]
                sumY = clusters[eachClust][ptInClust][1]
                size = len(clusters[eachClust])
            elif(len(clusters[eachClust]) <= 0) : # if 0 pts in cluster
                size = len(clusters[eachClust])+1
                sumX = random.uniform(XMIN,XMAX)
                sumY = random.uniform(YMIN,YMAX)
        print("Cluster size: " + str(size) + " sum X: " + str(sumX))
        CENTROID.append([sumX/size, sumY/size]) #calculate avg of points in each cluster
        print("length: " + str(len(clusters)) + " Index: " + str(eachClust))
    for center in CENTROID:
        print(center)

def converge(file, iteration):
    diffX = 0
    diffY = 0
    step = 0
    shift = []
    readIntoFile(file)
    generateInitialK()
    assignCluster()
    clusterAvg(step)

    i = 0
    #repeat assignment of points to clusters and averaging new centroids if difference between centroids is above acceptable limit
    #or keep repeating until number of iterations is complete.
    while(i <= iteration):
        i +=1
        step += K #to know which clusters to check avg of. iterate over last K clusters
        assignCluster()
        clusterAvg(step)
        print("Index: "+ str(i))
    print("Step: "+ str(step))


def scale(n, start1, stop1, start2, stop2):
    #maps the points so that all ranges fit in the screen
    return (n-start1)/ (stop1-start1)*(stop2-start2)+start2

def graph(): #plot with plotly
    global running;
    global XMIN, XMAX, YMIN, YMAX
    colours = [(255,0,0) , (0,255,0), (0,0,255), (255,0,255), (0,255,255), (230,230,0)]

    #start pygame
    pygame.init()

    #set window size and title
    screen = pygame.display.set_mode((win['width'], win['height']))
    pygame.display.set_caption("K Mean Cluster")

    while running:
        #check if window is closed or quit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))

        #draw an image and invert colours
        graph = pygame.Surface((win['width'], win['height']), pygame.SRCALPHA, 32)
        graph = graph.convert_alpha()

        # [# of centroids/cluster][# pts in cluster][x,y]
        c = 0
        for i in range(len(clusters)-1, len(clusters)-(1+K),-1):
            for j in range(0,len(clusters[i])):
                # scale points in cluster
                pt = (int(scale(clusters[i][j][0], XMIN, XMAX, 0-5, win['width']-5)),
                int(scale(clusters[i][j][1], YMIN, YMAX, 0+5, win['height']-5)))
                # draw points in cluster
                pygame.draw.circle(graph, colours[c], pt, 5, 0)
            c += 1
            # scale centroid
            k_pt = (int(scale(CENTROID[i][0], XMIN, XMAX, 0+8, win['width']-8)),
            int(scale(CENTROID[i][1], YMIN, YMAX, 0+8, win['height']-8)))
            # draw centroid
            pygame.draw.circle(graph, (0,0,0), k_pt, 8, 0)

        # flip image vertically so it's the correct orientation
        graph = pygame.transform.flip(graph, False, True)
        # scale image down to 95%
        graph = pygame.transform.scale(graph, (int(0.95*win['width']), int(0.95*win['height'])))
        # draw image to another image (double buffering)
        screen.blit(graph, (0,0))
        #draw the buffered image to screen
        pygame.display.flip()
    pygame.quit()

#user input for filename, iterations, no. clusters
file = raw_input("Enter filename (csv): ")
iteration = input("Enter iterations: ")
K_in = input("Enter number of clusters: ")
while int(K_in) > 6 or int(K_in) < 2:
    K_in = input("INVALID. Enter number of clusters (must be between 2-6): ")
K = int(K_in)

#timer for length of time it takes to calculate
startTime = time.time()
converge(str(file), int(iteration))
endTime = time.time()
graph()

print("Num Points: " + str(len(COORDINATES)))
print("Time Elapsed: " + str(endTime - startTime))
#fin
