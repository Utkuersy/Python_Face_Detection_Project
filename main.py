import cv2
import os

# Load the Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Directory to save detected face images
save_dir = "saved_faces"
os.makedirs(save_dir, exist_ok=True)

# Start the webcam
cap = cv2.VideoCapture(0)

# List to store coordinates of already saved faces
saved_faces_coords = []

# Function to check if a face is already saved (based on coordinates)
def is_new_face(x, y, w, h):
    for (sx, sy, sw, sh) in saved_faces_coords:
        if abs(x - sx) < 20 and abs(y - sy) < 20:
            return False
    return True

face_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Save only new faces
        if is_new_face(x, y, w, h):
            face_count += 1
            face_img = frame[y:y+h, x:x+w]
            face_path = os.path.join(save_dir, f"face_{face_count}.png")
            cv2.imwrite(face_path, face_img)
            saved_faces_coords.append((x, y, w, h))
            print(f"[+] Saved new face: {face_path}")

        # Draw rectangle around face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the webcam feed
    cv2.imshow("Face Detection", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
