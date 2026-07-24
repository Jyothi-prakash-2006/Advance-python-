import cv2

def open_camera():
    # Initialize the video capture object. 
    # '0' usually refers to the default built-in laptop webcam.
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    print("Camera opened successfully. Press 'q' to quit.")

    while True:
        # Read a single frame from the camera
        ret, frame = cap.read()

        # If the frame wasn't read correctly, exit the loop
        if not ret:
            print("Error: Failed to grab frame.")
            break

        # Display the resulting frame in a window
        cv2.imshow('Live Camera Feed', frame)

        # Wait for 1 millisecond and check if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    open_camera()