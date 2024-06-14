import cv2
import torch
import time 
from lib64 import jkrc

# Load custom model 
model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/Cutshion/Desktop/ReposDesktop/spin/yolov5/runs/train/exp3/weights/best.pt')

# Connect to robot
robot = jkrc.RC("10.5.5.100")  # Adjust IP address
robot.login()
robot.power_on()
robot.enable_robot()

# Robot movement function
def move_robot():
    joint_pos = [0.1636544625046775, 0.05835368727702882, 1.0094548061222204, 0.04662385297315052, 1.9225637723429245, 0.9997486810860294]
    robot.joint_move(joint_pos, 0, True, 1)  
    
    # Activate digital output 1 on the tool IO
    ret = robot.set_digital_output(1, 1, 1)  #TOOL, INDEXTOOL, T/F
    if ret[0] == 0:
        print("Digital output 1 activated successfully.")
    else:
        print(f"Error activating digital output 1, error code: {ret[0]}")
    
    # Check the status of the digital output after setting it
    time.sleep(0.1)  # Wait for the output to settle
    ret = robot.get_digital_output(1, 1)
    if ret[0] == 0:
        print(f"Status of digital output 1 is: {ret[1]}")
    else:
        print(f"Error checking status of digital output 1, error code: {ret[0]}")
# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Determine the new width (e.g., half of the original width)
    original_width = frame.shape[1]
    new_width = original_width // 6

    # Calculate the starting and ending x coordinates to crop the frame
    start_x = (original_width - new_width) // 2
    end_x = start_x + new_width

    # Crop the frame to focus on the middle
    cropped_frame = frame[:, start_x:end_x]

    # Make predictions on the cropped frame
    results = model(cropped_frame)

    # Draw bounding boxes and check for class ID 15
    for det in results.xyxy[0]:  # detections per image
        if int(det[5]) == 15:  # Check if the detected class is 15
            move_robot()  
            # Extract bounding box coordinates
            x1, y1, x2, y2 = int(det[0]), int(det[1]), int(det[2]), int(det[3])
            # Draw rectangle
            cv2.rectangle(cropped_frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            # display class and confidence
            cv2.putText(cropped_frame, f'Class: {int(det[5])}, Conf: {det[4]:.2f}', (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            break  

    # Display the frame with bounding boxes
    cv2.imshow('Webcam', cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()