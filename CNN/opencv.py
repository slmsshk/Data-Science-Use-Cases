import cv2
import numpy as np

im = cv2.imread('download.webp')
cv2.imshow('Image', im)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convert to grayscale
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray)
cv2.waitKey(0)

# Detect edges using Canny
edges = cv2.Canny(gray, 100, 200)
cv2.imshow('Edges', edges)
cv2.waitKey(0)

# Detect corners using Harris Corner Detection
gray_float = np.float32(gray)
corners = cv2.cornerHarris(gray_float, 2, 3, 0.04)
corners = cv2.dilate(corners, None)
im[corners > 0.01 * corners.max()] = [0, 0, 255]
cv2.imshow('Corners', im)
cv2.waitKey(0)

# Detect objects using contours
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im, contours, -1, (0, 255, 0), 3)
cv2.imshow('Contours', im)
cv2.waitKey(0)

cv2.destroyAllWindows()