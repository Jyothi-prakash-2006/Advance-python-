import cv2

# Read image
image = cv2.imread("input.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect edges
edges = cv2.Canny(gray, 100, 200)

# Save output
cv2.imwrite("edges.jpg", edges)

print("Edges detected successfully!")
