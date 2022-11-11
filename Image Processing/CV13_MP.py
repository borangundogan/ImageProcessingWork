import cv2
print(cv2.__version__)

class mpPose:
    import mediapipe as mp
    def __init__(self,still=False,upperBody=False, smoothData=True, tol1=.5, tol2=.5, maxComplexity= 1):
        self.myPose=self.mp.solutions.pose.Pose(still,upperBody,maxComplexity,smoothData,tol1,tol2)
    def Marks(self,frame):
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.myPose.process(frameRGB)
        poseLandmarks=[]
        if results.pose_landmarks:
            for lm in results.pose_landmarks.landmark:            
                poseLandmarks.append((int(lm.x*width),int(lm.y*height)))
        return poseLandmarks

class mpHands:
    import mediapipe as mp
    def __init__(self,condition = False,maxHands = 2, modelComplexity = 1 , confidentDetect = 0.5, confidentTrack = 0.5):
        self.hands = self.mp.solutions.hands.Hands(condition,maxHands,modelComplexity,confidentDetect,confidentTrack)
    def Marks(self,frame):
        self.frame = frame
        myHands = []
        
        self.frameRGB = cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGB)
        self.result =  self.hands.process(self.frameRGB)

        if self.result.multi_hand_landmarks != None:
            for handLandMarks in self.result.multi_hand_landmarks:
                myHand = []
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*width) , int(landMark.y*height)))
                print(myHand)
                myHands.append(myHand)
                
        return myHands

width=640
height=360
fps = 75
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, fps)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

findHands=mpHands(2)
findPose=mpPose()

while True:
    ignore,  frame = cam.read()
    #frame=cv2.resize(frame,(width,height))
    handData=findHands.Marks(frame)
    for hand in handData:
        for ind in [0,5,6,7,8]:
            cv2.circle(frame,hand[ind],25,(255,0,255),3)
    poseData=findPose.Marks(frame)
    if len(poseData)!=0:
        cv2.circle(frame,poseData[0],5,(0,255,0),3)

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()