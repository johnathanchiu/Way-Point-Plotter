### This package plots 3D waypoints in 2D space in real time or on a pre-recorded image/video ###
### Follow the README.md to figure out how to achieve either function ###


import cv2
import numpy as np


class ProjectPlot:

    def __init__(self, rotationMatrix, distortionCo, translationMatrix, cameraMatrix):
        self.rotation = rotationMatrix
        self.distortion = distortionCo
        self.translation = translationMatrix
        self.camera = cameraMatrix

    def visualize_plotter(self, image, object_points, debug=True):
        im = cv2.imread(image)     # uncomment this line and comment the line below to plot waypoints on a pre-recorded image
        #im = image
        if debug: print("object in 3d: ", object_points)
        projection_2d = np.squeeze(self.object3d_to_object2d(object_points))
        projection_2d = np.reshape(projection_2d, (1, projection_2d.shape[0] * 2))[0] * 100
        if debug: print("object in 2d: ", projection_2d)
        count = 0
        while count < len(projection_2d):
            x_val, y_val = int(projection_2d[count]), int(projection_2d[count+1])
            im[:, :, 0][x_val-20:x_val+20, y_val-20:y_val+20], im[:, :, 1][x_val-20:x_val+20, y_val-20:y_val+20], im[:, :, 2][x_val-20:x_val+20, y_val-20:y_val+20] = 255, 255, 255
            count += 2
        #cv2.imwrite("filename", im)  # uncomment this line if you want to save your video frames
        im = cv2.resize(im, (960, 540)) # you can adjust the size of the image you see accordingly
        cv2.imshow('image', im)
        cv2.waitKey(1)
        return projection_2d

    # function changes 3d waypoint to 2d waypoint
    def object3d_to_object2d(self, object_points):
        points_3d = np.array([object_points], dtype=float)
        projectionPoints, _ = cv2.projectPoints(points_3d, self.rotation, self.translation, self.camera, self.distortion)
        return projectionPoints

    ### access the camera and plot the object points in real-time ###
    def access_cam(self, object_points):
        cap = cv2.VideoCapture(0) # change the argument of this function according to the port your camera is plugged into

        # Check if the webcam is opened correctly
        if not cap.isOpened():
            raise IOError("Cannot open webcam")

        while True:
            ret, frame = cap.read()
            frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            self.visualize_plotter(frame, object_points)
            cv2.imshow('Input', frame)

        cap.release()
        cv2.destroyAllWindows()






