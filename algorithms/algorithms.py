import numpy as np

def rgb2gray(image):
    assert image.shape[2] == 3
    return np.mean(image, axis=2)