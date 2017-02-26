import cv2,socket,numpy
import time

host='192.168.1.100'
port=5565

cap=cv2.VideoCapture(0)
while True:
        ret,frame=cap.read()
        rval,imgencode=cv2.imencode("*.jpg",frame)
        data=numpy.array(imgencode)
        stringData=data.tostring()

        s=socket.socket()
        s.connect((host,port))
        s.sendall(stringData)
        s.close()
        time.sleep(0.3)
