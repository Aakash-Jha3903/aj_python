import cv2
import mediapipe as mp
import pyttsx3
import time

# Initialize Face Mesh and Drawing utils
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def animate_face():
    cap = cv2.VideoCapture(0)  # Open webcam
    with mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = face_mesh.process(rgb_frame)
            
            if result.multi_face_landmarks:
                for face_landmarks in result.multi_face_landmarks:
                    mp_drawing.draw_landmarks(frame, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION)
            
            cv2.putText(frame, "Speaking...", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("Animated Avatar", frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    text = input("Enter text to speak: ")
    speak(text)
    animate_face()
