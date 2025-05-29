import cv2 as cv
import numpy as np

"""
# Displaying images

img = cv.imread('temp_photos/dips_photo.png') # Selecting the File
cv.imshow('Cat', img) #Displaying image
cv.waitKey(0) # Wait for 0 press to close the window
"""


"""
# Displaying Videos

capture = cv.VideoCapture('videos/TheFall.mp4') # Seleciing the video

while True:
    isTrue, frame = capture.read() # Reading the video frame by frame
    cv.imshow('Video', frame) # Displaying the video frame

    if cv.waitKey(20) & 0xFF == ord('d'): # Press 'd' to stop the video
        break

# If you get a -215 error, it means the video file is not found or the path is incorrect

capture.release() # Releasing the video capture
cv.destroyAllWindows() # Destroying all windows
"""

blank = np.zeros((500,500,3), dtype='uint8') # Creating a blank image
cv.imshow('Blank', blank) # Displaying the blank image

blank[:] = 255, 0, 0 # Changing the color of the blank image to blue
cv.imshow('Blue', blank) # Displaying the blue image ('Name of Window', image)

blank[200:300 300:400] = 255, 0, 0 # Changing the color of the blank image to blue
cv.imshow('square', blank) # Displaying the blue image ('Name of Window', image)

cv.waitKey(0) # Wait for 0 press to close the window

