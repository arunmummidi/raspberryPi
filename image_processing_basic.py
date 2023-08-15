import cv2

# Load the image
img = cv2.imread("/home/arunodaya/2.jpeg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply edge detection
edges = cv2.Canny(gray, 100, 200)

# Find contours of objects
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Loop through the contours to count vehicles
vehicle_count = 0
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 500:  # adjust the area threshold as per your image
        vehicle_count += 1

# Show the image with contours
#cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
#cv2.imshow("Image with contours", img)
#cv2.waitKey(0)

# Print the vehicle count
print("Number of vehicles:", vehicle_count)
