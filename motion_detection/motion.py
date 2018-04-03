#!/usr/bin/env python

import sys
import pygame
import pygame.camera
import numpy as N
import pygame.surfarray

running  = True

previousFrame = None
isFirstFrame = True

win = {
    "width":640,
    "height":480
}

def luminenceCalc(r, g, b):
    return  0.3 * r + 0.59 * g + 0.11 * b

def convertToGrayscale(surfArr):
    weights = N.array([0.3, 0.59, 0.11])
    surfArr[:,:,0] = luminenceCalc(surfArr[:,:,0], surfArr[:,:,1], surfArr[:,:,2])
    surfArr[:,:,1] = luminenceCalc(surfArr[:,:,0], surfArr[:,:,1], surfArr[:,:,2])
    surfArr[:,:,2] = luminenceCalc(surfArr[:,:,0], surfArr[:,:,1], surfArr[:,:,2])
    return surfArr.astype(N.int8)

#start pygame
pygame.init()
#start camera
pygame.camera.init()
#load list of cameras available
cameras = pygame.camera.list_cameras()
#select the first one because it is most likely the correct one
cam = pygame.camera.Camera(cameras[0])
#start the camera, begin image stream
cam.start()

#create window with defined width/height
screen = pygame.display.set_mode((win['width'],win['height']))
# add a title to make it look pretty
pygame.display.set_caption("SOFE2715 - Motion Detection")

#begin main loop
while running:
    for event in pygame.event.get():
		if event.type == pygame.QUIT: running = False
    currentFrame = N.array(pygame.surfarray.array3d(cam.get_image()))
    screen.fill((0,0,0))
    if (not isFirstFrame):
        frameDiff = abs(convertToGrayscale(previousFrame) - convertToGrayscale(currentFrame))
        arrMap = N.where(frameDiff > 150)
        print(len(arrMap))
        pygame.surfarray.blit_array(screen, frameDiff)
    else:
        isFirstFrame = False
    pygame.display.flip()
    previousFrame = N.copy(currentFrame)
cam.stop()
pygame.quit()
