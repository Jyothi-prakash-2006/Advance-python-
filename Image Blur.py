import cv2

# Read image
image = cv2.imread("input.jpg")

# Apply Gaussian blur
blurred = cv2.GaussianBlur(image, (15, 15), 0)

# Save output
cv2.imwrite("blurred.jpg", blurred)

print("Image blurred successfully!")
