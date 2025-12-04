import cv2
import os

def video_to_frames(output_folder="frames"):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture("Bad-apple.mp4")

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    frame_count = 0

    while True:
        success, frame = cap.read()
        if not success:
            break  # No more frames

        frame_count += 1
        # Format number as 4 digits (0001, 0002, etc.)
        filename = f"{frame_count:04}.png"
        filepath = os.path.join(output_folder, filename)

        cv2.imwrite(filepath, frame)

    cap.release()
    print(f"Done! Extracted {frame_count} frames to '{output_folder}'.")

video_to_frames()