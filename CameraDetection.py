import cv2
import torch

# Load the model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/Cutshion/Desktop/ReposDesktop/spin/yolov5/runs/train/exp3/weights/best.pt')
# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

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

    # Draw the predictions on the cropped frame
    images = results.render()  # updates results.imgs with boxes and labels

    for img in images:
        cv2.imshow('Webcam', img)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()