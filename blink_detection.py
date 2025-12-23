import cv2
import time

# Load Haar cascades
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml'
)

cap = cv2.VideoCapture(0)

blink_count = 0
eyes_closed = False
last_blink_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)

        if len(eyes) == 0 and not eyes_closed:
            eyes_closed = True
            blink_count += 1
            last_blink_time = time.time()

        if len(eyes) > 0:
            eyes_closed = False

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.putText(frame, f"Blinks: {blink_count}", (30, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Blink Detection - LIS (OpenCV)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("\nDetected Message:")
if blink_count == 1:
    print("I need water")
elif blink_count == 2:
    print("I need food")
elif blink_count >= 3:
    print("I want to go to the washroom")
else:
    print("No blinks detected")
