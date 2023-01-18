import numpy as np
import cv2, dlib
import sys
from math import atan2, degrees

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

#detector : 이미지의 얼굴을 인식하여 위치를 잡아주는 기능
#predictor: 'shape_predictor_68_face_landmarks.dat'모델을 통해
# 얼굴에 68개의 좌표를 찍어주는 기능

cap = cv2.VideoCapture('NewJeans.mp4')
# 웹캠을 cap에 저장

scaler = 0.5

while True:
    frame, img = cap.read()

    if not frame:
        break

    img = cv2.resize(img,(int(img.shape[1] * scaler), int(img.shape[0] * scaler)))
    original = img.copy()

#얼굴 포인트 찾기
    try:
        faces = detector(img)
        face = faces[0]
    except:
        break

    dlib_shape = predictor(img,face)
    shape_2d = np.array([[p.x,p.y] for p in dlib_shape.parts()])

    top_left = np.min(shape_2d, axis=0)
    bottom_right = np.max(shape_2d,axis=0)

    center_X, center_Y = np.mean(shape_2d ,axis=0).astype(np.int)
    
    #얼굴 포인트 시각화
    for i in shape_2d:
        cv2.circle(img,center = tuple(i),radius=1,color=(255,255,255),
                    thickness=2, lineType=cv2.LINE_AA)

    cv2.circle(img, center=tuple(top_left),radius=1, color=(255,1,1),
                thickness=2,lineType=cv2.LINE_AA)
    cv2.circle(img, center=tuple(bottom_right),radius=1, color=(255,1,1),
                thickness=2,lineType=cv2.LINE_AA)
    cv2.circle(img, center=tuple((center_X,center_Y)),radius=1, color=(255,1,1),
                thickness=2,lineType=cv2.LINE_AA)

    cv2.imshow('img',img)
    cv2.waitKey(1)
    if cv2.waitKey(1) == ord('q'):
        sys.exit(1)



