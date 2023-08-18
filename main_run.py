import os
import numpy as np

from matplotlib import pyplot as plt

from algorithms import *

image = plt.imread('./data/set14/baboon.png')
grayscale = rgb2gray(image)

path = './results/'
os.makedirs(path, exist_ok=True)

plt.figure(figsize=(8,8))
plt.imshow(image, vmin=0, vmax=1)
plt.axis(False)
plt.savefig(path + 'image.png', format='png', bbox_inches='tight')

plt.figure(figsize=(8,8))
plt.imshow(grayscale, vmin=0, vmax=1, cmap='gray')
plt.axis(False)
plt.savefig(path + 'grayscale.png', format='png', bbox_inches='tight')