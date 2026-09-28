import cv2

# Open video
video = cv2.VideoCapture("input.mp4")

frame_count = 0

while True:
    ret, frame = video.read()

    if not ret:
        break

    # Save every 30th frame
    if frame_count % 30 == 0:
        filename = f"frame_{frame_count}.jpg"
        cv2.imwrite(filename, frame)

    frame_count += 1

video.release()

print("Frames extracted successfully!")
