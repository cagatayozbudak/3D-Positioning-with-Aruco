# 1-) 
Requirements
Before running this code, ensure the following requirements are met:


Python 3.x
OpenCV library (cv2)
A camera (webcam) connected to your computer
Install Python and OpenCV

Usage
When the script is executed, the camera will open, and it will attempt to detect ArUco markers.
Detected markers will be displayed on the screen within rectangles.
Press the 'q' key to exit the application.
Notes
Ensure the camera is working correctly and know the camera index for entering the code. If the camera cannot be opened, check the connections.
You can generate various ArUco markers for testing here.

# 2-) 
Requirements
Before running this code, ensure the following requirements are met:

Python 3.x
OpenCV library (cv2)
NumPy
Matplotlib
A camera (webcam) connected to your computer

Installation
Install Python and Required Libraries

Usage
When the script is executed, it will:
Open the camera and attempt to detect ArUco markers in real-time.
Visualize a 3D cube whose movement is based on the detected ArUco marker.
Press the 'q' key to exit the application if needed.

Notes

Camera Calibration: The script uses a default camera matrix and distortion coefficients. For more accurate tracking, you may need to calibrate your camera and replace the default values (cameraMatrix and distCoeffs) with the calibration results.

Dynamic Plotting: You need to enable Qt5 in your Python environment to view the dynamic 3D plot. In some environments (like some IDEs), you may need to go to Preferences/Settings and select Qt5 as the plotting backend. Otherwise, the 3D visualization may not work properly.
Testing ArUco Markers: To test the script, you can generate ArUco markers from this online generator. Print or display the markers on a screen to use them in front of the camera.

Troubleshooting:
If the camera cannot be accessed, ensure it is properly connected and not being used by another application.
If you see an empty 3D plot, ensure the ArUco marker is within the camera's view.

https://www.youtube.com/watch?v=uogDPZadyVw (ex. video lang:turkish)

