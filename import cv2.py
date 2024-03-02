import cv2

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    cv2.imshow("age-gender", frame)
    k = cv2.waitKey(1)  # Wait for a key press for 1 millisecond
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

