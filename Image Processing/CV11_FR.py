import cv2 as cv
import face_recognition as FR

font=cv.FONT_HERSHEY_SIMPLEX

width = 640
height = 360
fps = 100

cap = cv.VideoCapture(0, cv.CAP_DSHOW)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv.CAP_PROP_FPS, fps)
cap.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc(*"MJPG"))

boranFace=FR.load_image_file('Photos/boran.jpg')
faceLoc=FR.face_locations(boranFace)[0]
boranFaceEncode=FR.face_encodings(boranFace)[0]

umutFace=FR.load_image_file('Photos/umut2.png')
faceLoc2=FR.face_locations(umutFace)[0]
umutFaceEncode=FR.face_encodings(umutFace)[0]


knownEncodings=[boranFaceEncode , umutFaceEncode]
names=['Boran Gundogan', "ISMALMUT"]

while True:
    _, unknownFace = cap.read()

    #unknownFace=FR.load_image_file('Photos/umut2.png')
    unknownFaceRGB=cv.cvtColor(unknownFace,cv.COLOR_RGB2BGR)
    faceLocations=FR.face_locations(unknownFaceRGB)
    unknownEncodings=FR.face_encodings(unknownFaceRGB,faceLocations)


    for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
        top,right,bottom,left=faceLocation
        print(faceLocation)
        cv.rectangle(unknownFaceRGB,(left,top),(right,bottom),(255,0,0),3)
        
        name='Unknown Person'
        matches=FR.compare_faces(knownEncodings,unknownEncoding)
        print(matches)
        
        if True in matches:
            matchIndex=matches.index(True)
            print(matchIndex)
            print(names[matchIndex])
            name=names[matchIndex]
        cv.putText(unknownFaceRGB,name,(left,top),font,.75,(0,0,255),2)

    cv.imshow('My Faces',unknownFaceRGB)

    if cv.waitKey(1) & 0xff==ord("q"):
        break

cap.release()
cv.destroyAllWindows()
    