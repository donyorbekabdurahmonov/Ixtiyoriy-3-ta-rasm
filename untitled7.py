# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p1aN-eY6yEUrgYZ3Q6ii6cbKUxOZD6GE
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files


uploaded = files.upload()


image_name1 = list(uploaded.keys())[0]
img1 = cv2.imread(image_name1)
gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)


plt.imshow(gray_img1, cmap='gray')
plt.axis('off')
plt.show()

uploaded = files.upload()

image_name2 = list(uploaded.keys())[0]
img2 = cv2.imread(image_name2)
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

plt.imshow(gray_img2, cmap='gray')
plt.axis('off')
plt.show()

uploaded = files.upload()

image_name3 = list(uploaded.keys())[0]
img3 = cv2.imread(image_name3)
gray_img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)


plt.imshow(gray_img3, cmap='gray')
plt.axis('off')
plt.show()