# Virtual Paint with Hand Tracking

This project implements a virtual painting application using hand tracking. It allows users to draw and erase on a virtual canvas using their hand gestures captured through a webcam.

## Functionality

The application offers the following functionalities:

* **Color Selection:** Users can choose different drawing colors from a designated area on the screen.
* **Brush Thickness Control:** The thickness of the brush can be adjusted using a slider displayed on the side of the canvas.
* **Eraser:** Users can erase unwanted drawings using their hand gestures.
* **Eraser Thickness Control:** Similar to the brush, the eraser thickness can also be adjusted.

## Dependencies

The code relies on the following external libraries:

* OpenCV (cv2)
* NumPy (np)
* os
* MediaPipe (https://ai.google.dev/edge/mediapipe/solutions/guide)
* handtrackingmodule.py (**Note:** This module needs to be created based on MediaPipe hand tracking)

## Usage

1. Make sure you have OpenCV, NumPy, and `handtrackingmodule.py` installed. You'll also need to install MediaPipe following the official instructions (https://ai.google.dev/edge/mediapipe/solutions/guide).
2. Place the code in a Python file named `main.py`.
3. Run the script using `python main.py`.

## Code Explanation

The code is divided into several sections:

**1. Setting Up:**

* Imports necessary libraries, including `mediapipe` for hand tracking.
* Defines paths to folders containing images and the hand tracking module.
* Initializes variables for brush and eraser thickness, color selection, and image canvas.
* Creates a MediaPipe hand detector object.

**2. Main Loop:**

* Captures video frames from the webcam.
* Flips the captured frame horizontally for a more natural drawing experience.
* Uses the MediaPipe hand detector to find hand landmarks in the frame.
* Analyzes finger positions to determine drawing mode (selection or drawing/erasing) and color selection.
* Based on the drawing mode and selected color/eraser, updates the virtual canvas accordingly.
* Displays the brush/eraser thickness control bars on the side.
* Overlays the selected color palette on top of the main window.
* Combines the virtual canvas with the original video frame to display the final output.

## Creating the handtrackingmodule.py

The `handtrackingmodule.py` file should be created to handle hand detection and fingertip landmark extraction using MediaPipe. You can find tutorials and code examples online to achieve this functionality using MediaPipe's Python API.

## Further Enhancements

* Implement additional drawing tools (e.g., shapes, lines).
* Allow saving and loading drawings.
* Refine hand tracking accuracy for a smoother drawing experience.

This README provides a basic overview of the code's functionality and usage. Feel free to modify and enhance it to better suit your project's specific needs.
