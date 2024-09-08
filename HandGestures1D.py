import cv2
from cvzone.HandTrackingModule import HandDetector
import keyboard

import warnings
warnings.filterwarnings('ignore')

def hand_gestures():
    detector = HandDetector(detectionCon=0.9, maxHands=1)

    source = 0
    cap = cv2.VideoCapture(source)
    cam_w, cam_h = 640, 480
    cap.set(3, cam_w)
    cap.set(4, cam_h)

    print("Camera Detected:", cap.isOpened())

    while True:
        success, img = cap.read()
        if not success:
            break

        img = cv2.flip(img, 1)
        hands, img = detector.findHands(img, flipType=False)

        if hands:
            lmList = hands[0]["lmList"]
            _, tmb_y = lmList[4][0], lmList[4][1]
            _, pnk_y = lmList[20][0], lmList[20][1]

            if tmb_y - pnk_y > 100:
                print("\rKey Pressed: Left ", end="")
                keyboard.release("left")
                keyboard.press("right")
                
            elif pnk_y - tmb_y > 100:
                print("\rKey Pressed: Right", end="")
                keyboard.release("right")
                keyboard.press("left")
            else:
                print("\rKey Pressed: None ", end="")
                keyboard.release("right")
                keyboard.release("left")

        q = cv2.waitKey(1)
        if q == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    hand_gestures()