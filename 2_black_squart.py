import cv2
from random import*
cap = cv2.VideoCapture(0)
'''list_example = [0, 1, 2, 3]
print(list_example[1:3])
exit'''
square_length = 100
while True:
    ret, frame = cap.read()
    print(frame.shape)
    #frame[height-100:,width-100: ]
    height, width, _ = frame.shape
    frame[height - 100:, width - 100:]=[randint(0,255), randint(0,255), randint(0,255)]
    frame[height - 100:,:100] = [randint(0,255), randint(0,255), randint(0,255)]
    frame[:100, :100] = [randint(0,255), randint(0,255), randint(0,255)]
    frame[:100,width-100:] = [randint(0,255), randint(0,255), randint(0,255)]
    frame[height//2-square_length//2:height//2 + square_length//2, width//2 - square_length//2:width//2 +square_length//2] = [randint(0,255), randint(0,255), randint(0,255)]
    cv2.imshow('camera', frame)
    key = cv2.waitKey(1)
    print(key)
    if key == ord(" "):
        break
cv2.destroyAllWindows()
cap.release()