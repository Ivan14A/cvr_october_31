import cv2
from pprint import pprint

cap = cv2.VideoCapture(0)

while True:
    #ret - получилось ли достать кадр
    #frame - сам кадр
    ret, frame = cap.read()
    #Название окна сам кадр
    cv2.imshow('camera', frame)
    print(ret)
    for el in frame:
        for i in el:
            print(i,end='')
    pprint((frame))
    # Ожидать нажатия клавишу 1 мс
    cv2.waitKey(1)
    break