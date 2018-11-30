import cv2
import numpy as np

### pass in image as a numpy array ###
def check_plots(waypoints, im, onPath=True):
    count = 0
    while count < len(waypoints):
        x_val, y_val = int(waypoints[count]), int(waypoints[count + 1])
        waypoint = np.array([x_val - 20, x_val + 20, y_val - 20, y_val + 20])
        average_right = np.average(100 * np.array(im[:,:,0][waypoint[0]+40:waypoint[1]+20,waypoint[2]:waypoint[3]]) +
                                   100 * np.array(im[:,:,1][waypoint[0]+40:waypoint[1]+20,waypoint[2]:waypoint[3]]) +
                                   100 * np.array(im[:,:,2][waypoint[0]+40:waypoint[1]+20,waypoint[2]:waypoint[3]]))
        average_left = np.average(100 * np.array(im[:,:,0][waypoint[0]-20:waypoint[1]-40,waypoint[2]:waypoint[3]]) +
                                  100 * np.array(im[:,:,1][waypoint[0]-20:waypoint[1]-40,waypoint[2]:waypoint[3]]) +
                                  100 * np.array(im[:,:,2][waypoint[0]-20:waypoint[1]-40,waypoint[2]:waypoint[3]]))
        average_top = np.average(100 * np.array(im[:,:,0][waypoint[0]:waypoint[1],waypoint[2]+40:waypoint[3]+20]) +
                                 100 * np.array(im[:,:,1][waypoint[0]:waypoint[1],waypoint[2]+40:waypoint[3]+20]) +
                                 100 * np.array(im[:,:,2][waypoint[0]:waypoint[1],waypoint[2]+40:waypoint[3]+20]))
        average_bot = np.average(100 * np.array(im[:,:,0][waypoint[0]:waypoint[1],waypoint[2]-20:waypoint[3]-40]) +
                                 100 * np.array(im[:,:,1][waypoint[0]:waypoint[1],waypoint[2]-20:waypoint[3]-40]) +
                                 100 * np.array(im[:,:,2][waypoint[0]:waypoint[1],waypoint[2]-20:waypoint[3]-40]))
        print(average_right, average_left, average_bot, average_top)
        average1, average2, average3 = abs(average_left - average_right), abs(average_left - average_bot), abs(average_left - average_top)
        if average1 + average2 + average3 >= 1:
            return False
        count += 2
    return onPath
