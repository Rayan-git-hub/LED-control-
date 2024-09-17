# LED-control-using-OpenCV and Arduino
This project uses OpenCV and CVZone in Python to detect hand gestures, via  webcamera, sending commands to an Arduino. The Arduino controls LEDs based on number of fingers visible, enabling real-time, interactive LED control through computer vision and serial communication between the Python program and Arduino.

# Key Components:
1.Hand Detection (MediaPipe and CVZone):

* The program captures live video using OpenCV (cv2.VideoCapture(0)) and sets the resolution to 1280x720 pixels.
* CVZone's HandDetector is initialized with a detection confidence of 0.7 to track the hand in real-time.
* It specifically looks for one hand (hands = detector.findRightHand(img)) and detects how many fingers are raised using the fingersUp method. This method outputs a list of binary values, with 1 representing an extended finger and 0 for a closed one.

# Serial Communication with Arduino:

* The Arduino, connected to the serial port (COM5), is configured to receive data at a baud rate of 9600.
* Every time the total number of raised fingers changes, the new value is sent to the Arduino (ser.write(str(total_fingers).encode())).
* The system uses the total number of raised fingers to control LED states (or other hardware connected to the Arduino).

# Visualization:

* The program continuously updates the live video feed with the number of detected fingers displayed on the screen using cv2.putText().
* Optionally, the code includes commented-out sections that would draw gridlines on the image, dividing it into regions for further use, possibly to track hand movement across the screen.

# Program Execution:

* The program runs in an infinite loop, continuously capturing frames, detecting hand gestures, and updating the Arduino with the finger count.
* The loop breaks if the ESC key (ASCII 27) is pressed, exiting the program and closing the video feed window.
