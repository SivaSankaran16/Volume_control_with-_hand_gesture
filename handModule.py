import cv2
import mediapipe as mp
import time





class handDetector():
    def __init__(self,mode=False,maxHAnds=2,detectionCon=0.5,TrackCon=0.5) :
        self.mode=mode
        self.maxHands=maxHAnds
        self.detectionCon=detectionCon
        self.trackCon=TrackCon

        self.mphands=mp.solutions.hands
        self.hands=self.mphands.Hands()
        self.mpdraw=mp.solutions.drawing_utils

    def FindHands(self,img,draw=True):

        imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.res=self.hands.process(imgrgb)
        if self.res.multi_hand_landmarks:
            # print(len(res.multi_hand_landmarks))
            for handLms in self.res.multi_hand_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(img,handLms,self.mphands.HAND_CONNECTIONS)
        return img
    def findPosition(self,img,handNo=0):
        lmList=[]
        if self.res.multi_hand_landmarks:
            myHand=self.res.multi_hand_landmarks[handNo]
            for id , lm in enumerate(myHand.landmark):
                # print(id,lm)
                h,w ,_=img.shape
                cx,cy=int(w*lm.x),int(h*lm.y)
                lmList.append([id,cx,cy])
                # print(id,cx,cy)
                

        return lmList
    


