import cv2
import os

# Path to the video file
video_path = '/home/selva/Downloads/videoplayback.mp4'
output_folder = 'frames'

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Load the video
cap = cv2.VideoCapture(video_path)

frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_path = os.path.join(output_folder, f'frame_{frame_count:04d}.jpg')
    cv2.imwrite(frame_path, frame)
    frame_count += 1

cap.release()
print(f"Extracted {frame_count} frames and saved in '{output_folder}'")