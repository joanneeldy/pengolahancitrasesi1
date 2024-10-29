# pip install numpy, imageio, matplotlib
import numpy as np
import imageio as img
import matplotlib.pyplot as plt

# Load image
image = img.imread(r'C:\Users\LENOVO\Downloads\Pengolahan Citra Sesi 1\source.jpg')

# Split image into RGB components
red = image[:,:,0]
green = image[:,:,1]
blue = image[:,:,2]

# Create empty arrays for colored images
imgRed = np.zeros_like(image)
imgGreen = np.zeros_like(image)
imgBlue = np.zeros_like(image)

# Assign respective colors to their images
imgRed[:,:,0] = red
imgGreen[:,:,1] = green
imgBlue[:,:,2] = blue

# Plot the images
plt.figure(figsize=(10, 10))

plt.subplot(4, 1, 1)
plt.title("Original Image")
plt.imshow(image)

plt.subplot(4, 1, 2)
plt.title("Red Channel")
plt.imshow(imgRed)

plt.subplot(4, 1, 3)
plt.title("Green Channel")
plt.imshow(imgGreen)

plt.subplot(4, 1, 4)
plt.title("Blue Channel")
plt.imshow(imgBlue)

plt.tight_layout()
plt.show()
