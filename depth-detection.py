from SimpleCV import *
import numpy as np

cam = Kinect()
depth = cam.getDepth()
width = depth.width
height = depth.height
screensize = width * height
threshold = 255

while True:
  depth = cam.getDepth()
  avgcolor = depth.meanColor()
  R, G, B = avgcolor
  if (R > 255 or B > 255 or G > 255):
    depth.drawText('Threshold Exceeded.')
  depth.show()
