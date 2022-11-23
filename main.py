import cv2 as cv
image = cv.imread('./images/new.png')
cv.imshow('image', image)
cv.waitKey(0)


# read videop

capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
