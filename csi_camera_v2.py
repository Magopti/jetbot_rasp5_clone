import time
import cv2
from picamera2 import Picamera2

# Initiera Picamera2
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"size": (640, 480)}))
picam2.start()

# Textinställningar för tidsstämpel
colour = (0, 255, 0)
font = cv2.FONT_HERSHEY_SIMPLEX
scale = 1
thickness = 2

while True:
    frame = picam2.capture_array()  # Hämta bildruta
    
    # Rotera 180 grader så kameran blir rättvänd
    frame = cv2.rotate(frame, cv2.ROTATE_180)

    # Lägg på tidsstämpel EFTER rotation
    timestamp = time.strftime("%Y-%m-%d %X")
    h, w, _ = frame.shape
    origin = (10, h - 10)  # nere till vänster
    cv2.putText(frame, timestamp, origin, font, scale, colour, thickness)

    # Visa bilden
    cv2.imshow("Camera", frame)

    # Avsluta på 'q'
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# Stäng ner kameran och GUI-fönster
picam2.stop()
cv2.destroyAllWindows()
