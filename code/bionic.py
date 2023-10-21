import cv2
import mediapipe as mp
import serial

# Open a serial connection to the Arduino
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Change 'COM3' to your Arduino's port

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Define your mapping parameters for each servo
servo_mapping = {
    1: (0, 360),  # Minimum and maximum angle for servo 1
    2: (30, 360),  # Minimum and maximum angle for servo 2
    3: (45, 360),  # Minimum and maximum angle for servo 3
    4: (0, 360),  # Minimum and maximum angle for servo 4
    5: (0, 360),  # Minimum and maximum angle for servo 5
    6: (0, 180),  # Minimum and maximum angle for servo 6
}

cap = cv2.VideoCapture(0)

def map_landmarks_to_servo(hand_landmarks):
    servo_positions = {}
    
    # Example mapping logic for each servo
    # Adjust this logic based on your specific requirements
    for servo_num, (min_angle, max_angle) in servo_mapping.items():
        # Calculate the servo angle based on hand landmarks
        # You can use different landmarks and their coordinates as needed
        landmark_index = min(4, len(hand_landmarks.landmark) - 1)  # Example: Use the middle finger landmark
        servo_angle = int((max_angle - min_angle) * hand_landmarks.landmark[landmark_index].y + min_angle)
        servo_positions[servo_num] = servo_angle
    
    return servo_positions

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            servo_positions = map_landmarks_to_servo(hand_landmarks)

            # Send servo control commands to the Arduino
            for servo_num, servo_position in servo_positions.items():
                command = f'{servo_num} {servo_position}\n'
                ser.write(command.encode())

            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow('Hand Tracking', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

hands.close()
cap.release()
cv2.destroyAllWindows()
ser.close()

