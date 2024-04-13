import cv2

# Load an image
img = cv2.imread('image.jpg')

# Apply a filter to the image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Display the original and filtered images
cv2.imshow('Original', img)
cv2.imshow('Filtered', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
