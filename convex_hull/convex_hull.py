#!/usr/bin/env python
import pygame
import random

running = True

win = {
    "width": 800,
    "height": 800
}


def orientation(p, q, r):
    val = ((q[1] - p[1]) * (r[0] - q[0])) - ((q[0] - p[0]) * (r[1] - q[1]))
    if val == 0:
        return 0
    if val > 0:
        return 1
    else:
        return 2


# start pygame
pygame.init()

# create window with defined width/height
screen = pygame.display.set_mode((win['width'], win['height']))
# add a title to make it look pretty
pygame.display.set_caption("SOFE2715 - Convex Hull")

# create array for points
pointArray = []
# define number of points to generate
numOfPoints = 100
# set shortest_x to width of window and an index of -1
shortest_x = (win['width'], -1)
# generate all points and check for left-most
for i in range(0, numOfPoints):
        # random x/y inside window
    x = random.randint(100, 700)
    y = random.randint(100, 700)
    # find shortest x (left-most)
    if (x < shortest_x[0]):
        shortest_x = (x, i)
        # add the new points to the array
    pointArray.append((x, y))

# add array for points that make convex-hull
hullArray = []
# start at left most
currentPoint = shortest_x[1]
# while loop until return to left-most
while True:
    # add the point to the hull array
    hullArray.append(pointArray[p])
    # next point inside pointArray
    searchPoint = (currentPoint + 1) % len(pointArray)
    # find most counter-clockwise point
    for i in range(0, len(pointArray)):
        if (orientation(pointArray[currentPoint], pointArray[i], pointArray[searchPoint]) == 2):
            # set current index to current most counter-clockwise point
            searchPoint = i
        # set current point to most counter-clockwise
    currentPoint = searchPoint
    # if we arrive back at the start, we have completed the convex hull
    if currentPoint == shortest_x[1]:
        break
# print the complete hull array
print hullArray
# begin main loop
while running:
    # check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # set the background to white
    screen.fill((255, 255, 255))
    # draw the convex-hull polygon
    pygame.draw.polygon(screen, (0, 0, 0), hullArray, 2)
    # draw all points in the point array
    for i in range(0, len(pointArray)):
        # if this point is the left-most, make it red
        if i == shortest_x[1]:
            c = (255, 0, 0)
        else:  # otherwise, black
            c = (0, 0, 0)
        # get point x/y from point array
        pnt = (pointArray[i][0], pointArray[i][1])
        # draw the point with radius 5
        pygame.draw.circle(screen, c, pnt, 5, 0)
    # update the screen interface
    pygame.display.flip()
# quit if we break the loop
pygame.quit()
