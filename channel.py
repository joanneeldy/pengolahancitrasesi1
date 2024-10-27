#pip install numpy
import numpy as np
import imageio as img
import matplotlib.pyplot as plt

image = img.imread("D:/source.jpg")

red = image[:,:,0]
green = image[:,:,1]
blue = image[:,:,2]

imgRed = np.zeros_like(image)
imgGreen = np.zeros_like(image)
imgBlue = np.zeros_like(image)

imgRed[:,:,0] = red
imgGreen[:,:,1] = green
imgBlue[:,:,2] = blue

plt.figure(figsize=(10,10))
plt.subplot(3,1,1)
plt.imshow(image)

plt.subplot(3,1,2)
plt.imshow(imgRed)

plt.subplot(3,1,3)
plt.title("Green")
plt.imshow(imgGreen)

plt.subplot(3,1,4)
plt.title("Blue")
plt.imshow(imgBlue)

plt.show()