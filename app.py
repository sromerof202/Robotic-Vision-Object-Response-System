import cv2
import torch
import pyrealsense2 as rs
import numpy as np
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
    joint_pos = [0.2926767057278819, 0.07354974547536784, -2.089534011360541, -3.136098706170365, -0.46572435573386767, 0.8105057718849379]
    robot.joint_move(joint_pos, 0, True, 5)  
    

# Configure depth and color streams from the RealSense camera
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Start streaming
pipeline.start(config)

try:
    while True:
        # Wait for a coherent pair of frames: depth and color
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()
        if not depth_frame or not color_frame:
            continue

        # Convert images to numpy arrays
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        # Apply the same cropping as before to the color image
        # Assuming you still want to crop the color image
        original_width = color_image.shape[1]
        new_width = original_width // 6
        start_x = (original_width - new_width) // 2
        end_x = start_x + new_width
        cropped_color_image = color_image[:, start_x:end_x]

        # Make predictions on the cropped color frame
        results = model(cropped_color_image)

        # Draw bounding boxes and check for class ID 15
        for det in results.xyxy[0]:  # detections per image
            if int(det[5]) == 15:  # Check if the detected class is 15
                move_robot()
                x1, y1, x2, y2 = int(det[0]), int(det[1]), int(det[2]), int(det[3])
                # Calculate the center of the bounding box
                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2
                # Get the depth at the center of the detected object
                depth = depth_frame.get_distance(center_x, center_y)
                # Convert depth to a real-world distance
                if depth > 0:  # Check if depth is valid
                    print(f"Detected object is {depth:.15f} feet away.")
                
                # Draw rectangle and display class, confidence, and depth
                cv2.rectangle(cropped_color_image, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.putText(cropped_color_image, f'Class: {int(det[5])}, Conf: {det[4]:.2f}, Depth: {depth:.3f}m', (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                break

        # Display the frame with bounding boxes
        cv2.imshow('Webcam', cv2.cvtColor(cropped_color_image, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    # Cleanup
    pipeline.stop()
    cv2.destroyAllWindows()