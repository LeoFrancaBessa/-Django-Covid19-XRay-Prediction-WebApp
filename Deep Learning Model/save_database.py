import numpy as np
import cv2
import os

CATG = ['normal', 'covid', 'pneumonia']

def create_data(DIR):
  IMG_SIZE = 100 #resize size
  train_data = [] # array of images

  for category in CATG:
      class_num = CATG.index(category) # classifica como 0, 1 ou 2
      path = os.path.join(DIR, category) #path to dir
      for i, img in enumerate(os.listdir(path)): #iterate over files in folder
          try:
            img = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE) #read image in gray
            img = cv2.resize(img, (IMG_SIZE,IMG_SIZE)) #resize
            train_data.append([img, class_num]) #add to array
          except:
            pass

  return train_data


train = create_data(r'C:\Users\Leo\Desktop\Machine Learning\End-to-End Projects\X-Ray\Deep Learning Model\Dataset\train')
test = create_data(r'C:\Users\Leo\Desktop\Machine Learning\End-to-End Projects\X-Ray\Deep Learning Model\Dataset\test')

np.save('train.npy', train) 
np.save('test.npy', test)