import pickle

import cv2

from utils import get_face_landmarks


emotions = ['HAPPY', 'SAD', 'SURPRISED']

with open('./smodel', 'rb') as f:
    model = pickle.load(f)

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

while ret:
    ret, frame = cap.read()

    face_landmarks = get_face_landmarks(frame, draw=True, static_image_mode=False)
    #print(face_landmarks)
    
    #print(len(face_landmarks))
    if (len(face_landmarks) > 1400):
        output = model.predict([face_landmarks])
        #print(output)
        cv2.putText(frame,
                    emotions[int(output[0])],
                (10, frame.shape[0] - 1),
                cv2.FONT_HERSHEY_SIMPLEX,
                3,
                (0, 255, 0),
                5)
    
        cv2.imshow('frame', frame)

        cv2.waitKey(25)


cap.release()
cv2.destroyAllWindows()



'''

'''