import cv2

# 打开视频文件
cap = cv2.VideoCapture('3.mp4')

i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('.\\3\\frame'+str(i)+'.png', frame)
    i+=1

cap.release()
cv2.destroyAllWindows()