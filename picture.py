import cv2
import numpy as np

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Could not open camera")
    exit()

# Get camera dimensions
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Separate drawing canvas
canvas = np.zeros((height, width, 3), dtype=np.uint8)

# Drawing variables
drawing = False
last_x = None
last_y = None

# Brush settings
brush_color = (0, 0, 255)   # Red in BGR
brush_size = 5


def mouse_callback(event, x, y, flags, param):
    global drawing, last_x, last_y

    # Left mouse/trackpad click
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        last_x = x
        last_y = y

    # Move while clicking/dragging
    elif event == cv2.EVENT_MOUSEMOVE and drawing:

        cv2.line(
            canvas,
            (last_x, last_y),
            (x, y),
            brush_color,
            brush_size,
            cv2.LINE_AA
        )

        last_x = x
        last_y = y

    # Release click
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        last_x = None
        last_y = None


# Create window
window_name = "Camera Drawing"

cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name, mouse_callback)


while True:

    # Read camera
    ret, frame = cap.read()

    if not ret:
        print("❌ Failed to read camera")
        break

    # Mirror camera
    frame = cv2.flip(frame, 1)

    # Combine camera and drawing
    output = cv2.add(frame, canvas)

    # Show result
    cv2.imshow(window_name, output)

    # Keyboard controls
    key = cv2.waitKey(1) & 0xFF

    # Q = quit
    if key == ord('q'):
        break

    # C = clear drawing
    elif key == ord('c'):
        canvas[:] = 0

    # E = eraser
    elif key == ord('e'):
        brush_color = (0, 0, 0)
        brush_size = 30

    # R = red brush
    elif key == ord('r'):
        brush_color = (0, 0, 255)
        brush_size = 5

    # B = blue brush
    elif key == ord('b'):
        brush_color = (255, 0, 0)
        brush_size = 5

    # G = green brush
    elif key == ord('g'):
        brush_color = (0, 255, 0)
        brush_size = 5


# Close everything
cap.release()
cv2.destroyAllWindows()