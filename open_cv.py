import cv2

# Create a VideoCapture object to capture video from the default camera
cap = cv2.VideoCapture(0)

# Check if camera is opened successfully
if not cap.isOpened():
    print("Error opening camera")
    exit()

# Set the camera frame width and height
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create a window to display the camera feed
cv2.namedWindow('Camera', cv2.WINDOW_NORMAL)

# Loop until spacebar is pressed
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Resize the frame to half its original size
    frame = cv2.resize(frame, (int(frame_width/2  ), int(frame_height/2)))

    # Display the resulting frame
    cv2.imshow('Camera', frame)

    # Check if spacebar is pressed
    if cv2.waitKey(1) & 0xFF == ord(' '):
        # Save the image to a file
        cv2.imwrite('image.jpg', frame)
        print("Image captured!")
        break

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()
