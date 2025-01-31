import cv2
import numpy as np

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Create a blank image to draw on
canvas = np.zeros((480, 640, 3), dtype=np.uint8)

# Define the color and thickness of the brush
color = (255, 0, 0)
thickness = 5

# Function to draw on the canvas
drawing = False

def draw(event, x, y, flags, param):
    global drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        cv2.circle(canvas, (x, y), thickness, color, -1)
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        cv2.circle(canvas, (x, y), thickness, color, -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

# Set the mouse callback function
cv2.namedWindow('Webcam Paint')
cv2.setMouseCallback('Webcam Paint', draw)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Combine the frame and the canvas
    combined = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)

    # Display the resulting frame
    cv2.imshow('Webcam Paint', combined)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()