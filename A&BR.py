import cv2
import numpy as np
import pyrealsense2 as rs

# Configure depth and color streams
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Start streaming
profile = pipeline.start(config)

# Getting the depth sensor's depth scale
depth_sensor = profile.get_device().first_depth_sensor()                        
depth_scale = depth_sensor.get_depth_scale()

# Apply filters to depth data
spatial_filter = rs.spatial_filter()
temporal_filter = rs.temporal_filter()

iteration_count = 0
max_iterations = 2  # Set this to the desired number of iterations

roi_width = 320  
roi_height = 240  

try:
    while True:
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()
        if not depth_frame or not color_frame:
            continue

        # Apply filters
        depth_frame = spatial_filter.process(depth_frame)
        depth_frame = temporal_filter.process(depth_frame)

        # Convert images to numpy arrays
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        # Calculate the starting x and y coordinates to center the ROI
        start_x = (depth_image.shape[1] - roi_width) // 2
        start_y = (depth_image.shape[0] - roi_height) // 2

        # Crop the depth and color images to the ROI
        depth_image_roi = depth_image[start_y:start_y+roi_height, start_x:start_x+roi_width]
        color_image_roi = color_image[start_y:start_y+roi_height, start_x:start_x+roi_width]

        # Iterate through the entire depth image ROI
        for y in range(0, depth_image_roi.shape[0]):
            for x in range(0, depth_image_roi.shape[1]):
                depth_value = depth_image_roi[y, x] * depth_scale * 1000  # Convert to mm
                if  depth_image_roi[y, x] > 0 and depth_value < 155.00:  # Check if the depth value is greater than 0 and less than 155.00mm
                    # Print the x, y coordinates and depth information for each point
                    print(f"Point at ({x+start_x}, {y+start_y}) with depth: {depth_value:.2f}mm")
                    # Highlight the point in the color image ROI
                    cv2.circle(color_image_roi, (x, y), 2, (0, 255, 0), -1)

        # Display the color image ROI with all points highlighted
        cv2.imshow('All Points Highlighted', color_image_roi)

        if cv2.waitKey(1) & 0xFF == ord('q') or iteration_count >= max_iterations:
            break

        iteration_count += 1

finally:
    # Stop streaming
    pipeline.stop()
    cv2.destroyAllWindows()