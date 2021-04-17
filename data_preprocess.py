import numpy as np
import os
import pandas as pd
import cv2
import pickle
import ast
from builtins import object

class data_preprocess(object):
    def __init__(self, path, size= 128):
        self.path = path
        self.size = size
        
    #defining function to load data
    def load_images(self, size= 128):
        '''
        Function to load images using CV2 and resized to get them ready for training
        Arguments:
        imgPath-- Takes in path of the image as input
        size-- Takes in the required reduced size of image (optional)
        Return:
        images-- Images dataset with all the data features
        labels-- Target labels for all the images in image dataset extracted from the directory name
        '''
        images = list()
        labels = list()

        for subdir in sorted(os.listdir(self.path)):
            if subdir.strip().startswith('c'):
                subdir_path = os.path.join(self.path, subdir)

                for file in os.listdir(subdir_path):
                    if file.endswith('jpg'):
                        fpath = os.path.join(subdir_path,file)
                        img = cv2.imread(fpath)
                        img_resize = cv2.resize(img,(128,128))
                        images.append(img_resize)
                        labels.append(int(fpath.split('/')[-2].replace('c', '')))

        return images, labels