# Defining points on from a circular distribution 
import random
import math
# Now write a classifier that tells me which part of the board its on: 
# Region (n) is defined by: (x^2)+(y^2) <= {(1,5,10,>10)}
def score(x,y):
    region_classifier = (x*x)+(y*y)
    points = []
    if region_classifier <= 1: 
        points.append(10)
        print("The dart earned %s points" %(points[0]))
    points = []
    if region_classifier <= 25 and region_classifier > 1: 
        points.append(5)
        print("The dart earned %s points" %(points[0]) )
    points = []
    if region_classifier <= 100 and region_classifier > 25: 
        points.append(1)
        print("The dart earned %s points" %(points[0]) )
    points = []
    if region_classifier > 100 : 
        points.append(0)
        print("The dart earned %s points" %(points[0]) )
    points = []

def score_random(circle_r):
    # radius of the circle --> I.e. size of the backboard 
    # center of the circle (x, y)
    circle_x = 0
    circle_y = 0
    # random angle
    alpha = 2 * math.pi * random.random()
    # random radius
    r = circle_r * math.sqrt(random.random())
    # calculating coordinates
    x = r * math.cos(alpha) + circle_x
    y = r * math.sin(alpha) + circle_y
    x = round(x)
    y = round(y)
    region_classifier = (x**2)+(y**2)
    print("Random point", (x, y))
    region_classifier = (x*x)+(y*y)
    points = []
    if region_classifier <= 1: 
        points.append(10)
        print("The dart earned %s points" %(points[0]))
    points = []
    if region_classifier <= 25 and region_classifier > 1: 
        points.append(5)
        print("The dart earned %s points" %(points[0]) )
    points = []
    if region_classifier <= 100 and region_classifier > 25: 
        points.append(1)
        print("The dart earned %s points" %(points[0]) )
    points = []
    if region_classifier > 100 : 
        points.append(0)
        print("The dart earned %s points" %(points[0]) )
    points = []