import cv2 as cv

"""
Reading the image using the functions: imread, imshow, waitKey, destroyWindow
"""
win1= 'Akira kurosawa'

img= cv.imread('data/images/video1.jpg')
cv.imshow( win1, img )
cv.waitKey(0)

cv.destroyWindow(win1)

"""
Reading the Video frame by frame using the class: VideoCapture and functions: read, waitKey, ord, release, destroyallWindows
"""
video= cv.VideoCapture('data/videos/video1.mp4')
while (True):
  
  # Reading each frame and then showing it with the help of image show method
  isTrue, frame= video.read()
  cv.imshow('Akira Kurosawa', frame)

  # Using waitKey for delay and 0xFF for the pressing of letter d with the help of key pointer function ord
  if( (cv.waitKey(20) & 0xFF)==ord('d') ):
    break

video.release()
cv.destroyAllWindows()
