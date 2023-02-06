from skimage import io
import matplotlib.pyplot as plt
from skimage import util
from skimage import transform

start_im = io.imread('rotation.png')

rotated_img = transform.rotate(start_im, 6)

# Determine the shape of the rotated image
rows, cols = rotated_img.shape[:2]

# Set Crop Area
start_row = max(0, int(rows * 0.12))
end_row = min(rows, int(rows * 0.9))
start_col = max(0, int(cols * 0.1))
end_col = min(cols, int(cols * 0.95))

imcrp = rotated_img[start_row:end_row, start_col:end_col]

io.imsave('rotated_img.png', imcrp)
