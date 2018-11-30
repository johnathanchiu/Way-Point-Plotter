### run this code ###
### this project inherits from the ProjectPlot package ###


from ProjectPlot.ProjectPlotter import *
from ProjectPlot.CheckTraj import *
import numpy as np


object_point = [1000, 1000, 1000], [1100, 1200, 900] # test model, you can import your own 3d object waypoints
im_path = '/Users/johnathanchiu/Downloads/mask.png'

### adjust the below parameters according to your camera model ###
### The parameters needed are as follows: cameraMatrix, rotationMatrix, distortionCo, translationMatrix ###

cameraMatrix = np.array([[0.1993102988, 0.000000, 0.688289840],
                         [0.000000, 0.1989493358, 0.477240944],
                         [0.000000, 0.000000, 0.1000000]])

rotationMatrix, distortionCo, translationMatrix = np.array([[0, -1, 0],
                                                            [0, 0, -1],
                                                            [1, 0, 0]], dtype=float), \
                                                      np.array([-0.231874, -0.175971, -0.001385, -0.003774,
                                                                0.000000]), \
                                                      np.array([0, -1.5, 0])

# this line creates a ProjectPlot instance, pass in the necessary matrices to convert 3d waypoints to 2d waypoints
plotPoints = ProjectPlot(rotationMatrix, distortionCo, translationMatrix, cameraMatrix)


plots = plotPoints.visualize_plotter(im_path, object_point)
im = cv2.imread(im_path)
if check_plots(plots, im):
    print("car is on path")
else:
    print("car is not on path")
# uncomment this line and comment the line above to get real-time waypoint plotting
#plotPoints.access_cam(object_point)


""" The block of code below allows the user the pass in their video file url and plot waypoints on their video in real time """
"""
cap = cv2.VideoCapture('/Users/johnathanchiu/Downloads/lap1_setting2_10_21.avi')
video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("frames: ", video_length)

success, image = cap.read()
count = 0

while success:
    print("frame number: ", count)
    plotPoints.visualize_plotter(image, object_point)
    success, image = cap.read()
    count += 1
"""





