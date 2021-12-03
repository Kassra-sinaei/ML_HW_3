import cv2
import os
import numpy as np
from numpy.lib.function_base import average
import pandas as pd

def loadData():
    data = list("")
    label = list("")
    os.chdir("/home/kassra/ML/HW_3/data")
    folder = "Images"
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        # Extract Feature
        if img is not None:
            avg = averageColor(img)
            data.append([avg[0], avg[2]])
        # Assign Label
        if filename[0] == 'm':
                label.append(0)
        elif filename[0] == 'c':
            label.append(1)
        
    return np.array(data), np.array(label)

def averageColor(img):
    sum = np.zeros(3)
    height, width = img.shape[:2]
    for i in range(height):
        for j in range(width):
            sum += img[i][j]

    avg = sum/(height * width)
    return avg

if __name__ == "__main__":
    temp = loadData()
    print("data loaded successfully")
    print(temp)
    pass