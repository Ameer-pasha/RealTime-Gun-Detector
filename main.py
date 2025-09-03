import numpy as np
import cv2
import imutils
import datetime
import os
import json

# Check if cascade file exists
if not os.path.exists('cascade.xml'):
    print("Error: cascade.xml file not found!")
    exit()

gun_cascade = cv2.CascadeClassifier('cascade.xml')
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not open camera!")
    exit()

print("Gun Detection Started. Press 'q' to quit.")

detections = []
detection_count = 0

while True:
    ret, frame = camera.read()
    if not ret:
        break

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect guns
    guns = gun_cascade.detectMultiScale(gray, 1.3, 20, minSize=(100, 100))

    # If gun detected
    if len(guns) > 0:
        detection_count += 1
        timestamp = datetime.datetime.now()

        # Draw rectangles
        for (x, y, w, h) in guns:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Save screenshot
        screenshot_name = f"detection_{timestamp.strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(screenshot_name, frame)

        # Save to JSON
        detection_data = {
            "detection_id": detection_count,
            "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "guns_count": len(guns),
            "screenshot": screenshot_name,
            "coordinates": [[int(x), int(y), int(w), int(h)] for x, y, w, h in guns]
        }
        detections.append(detection_data)

        # Save JSON file
        with open('detections.json', 'w') as f:
            json.dump(detections, f, indent=2)

        print(f"Gun detected! Screenshot: {screenshot_name}")

        # Stop after first detection (as requested)
        break

    # Add timestamp
    cv2.putText(frame, datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

    # Show frame
    cv2.imshow("Gun Detection - Security Feed", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

print(f"Total detections: {detection_count}")
camera.release()
cv2.destroyAllWindows()