
from handModule import*
import cv2
import time
import math
import numpy as np
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
pTime=0
cTime=0
wCam,hCam=640,480
cap=cv2.VideoCapture(0)
dec=handDetector()
cap.set(3,wCam)
cap.set(4,hCam)

volRange = volume.GetVolumeRange()

minVol = volRange[0]
maxVol = volRange[1]
vol = 0
while True:
    success,img=cap.read()
    imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img=dec.FindHands(img)
    list=dec.findPosition(img,0)
    if len(list)!=0:
        x1,y1=list[4][1],list[4][2]
        x2,y2=list[8][1],list[8][2]
        cx,cy=(x1+x2)//2,(y1+y2)//2
        cv2.circle(img,(x1,y1),15,(254,0,150),cv2.FILLED)
        cv2.circle(img,(x2,y2),15,(254,0,150),cv2.FILLED)
        cv2.line(img,(x2,y2),(x1,y1),(254,0,150),3)
        cv2.circle(img,(cx,cy),15,(254,0,150),cv2.FILLED)
        lent=math.hypot(x2-x1,y2-y1)
        volBar = np.interp(lent, [50, 215], [400, 150])
        volPer = np.interp(lent, [100, 215], [0, 100])
        if lent<49:
            cv2.circle(img,(cx,cy),15,(24,0,150),cv2.FILLED)
            volume.SetMute(True,None)
        elif lent>225:
            
            volume.SetMute(False,None)
        else:
            volume.SetMute(False,None)
            vol = np.interp(lent, [50, 215], [minVol, maxVol])
            volume.SetMasterVolumeLevel(vol, None)
        cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
        cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), -1)
        cv2.putText(img, f'{int(volPer)}%', (40, 450), cv2.QT_FONT_NORMAL, 2, (255, 0, 0), 2)

    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.QT_FONT_NORMAL,3,(255,0,0),3)
    cv2.imshow('im',img)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
