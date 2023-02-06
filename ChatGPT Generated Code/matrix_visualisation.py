import cv2
import numpy as np

# Load the image
img = cv2.imread('image.jpg')

# Define the source and destination points for the transformation
src_points = np.float32(
    [[0, 0], [img.shape[1], 0], [0, img.shape[0]], [img.shape[1], img.shape[0]]])
dst_points = np.float32([[0, 0], [img.shape[1], 0], [int(
    0.33*img.shape[1]), img.shape[0]], [int(0.66*img.shape[1]), img.shape[0]]])

# Compute the perspective transformation matrix
matrix = cv2.getPerspectiveTransform(src_points, dst_points)

# Perform the perspective transformation
transformed_img = cv2.warpPerspective(
    img, matrix, (img.shape[1], img.shape[0]))

# Show the original and transformed images
cv2.imshow("Original Image", img)
cv2.imshow("Transformed Image", transformed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
