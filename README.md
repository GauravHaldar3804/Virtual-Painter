# Virtual Paint with Hand Tracking

This project implements a virtual painting application using hand tracking with OpenCV and Python. Users can interact with the canvas using their fingers to draw and erase.

## Features

* **Selection:** Choose drawing or erasing mode by raising two fingers (index and middle).
* **Color Selection:** Select different drawing colors from a designated area on the header.
* **Drawing:** Draw on the canvas using your index finger.
* **Erasing:** Erase parts of the drawing with a thicker "eraser" effect using your index finger.
* **Customization:** Adjust brush thickness and eraser size for a personalized experience (code modifications required).

## Requirements

* Python 3.x (https://www.python.org/downloads/)
* OpenCV library (`pip install opencv-python`)
* `handtrackingmodule.py` (custom module for hand detection and finger tracking)

## Usage

1. Clone or download the repository.
2. Install the required libraries: `pip install opencv-python`,`pip install mediapipe`
4. Ensure you have the `handtrackingmodule.py` file in the same directory as your main script.
5. Run the `main.py` script.

## Code Overview

**main.py**

The core script imports necessary libraries, defines variables, and performs the following tasks in a continuous loop:

1. **Image Capture:** Reads frames from the webcam.
2. **Hand Detection:** Uses the `handtrackingmodule` to detect hands and their landmarks.
3. **Finger Tracking:** Analyzes finger positions to determine drawing or erasing mode.
4. **Color Selection:** Updates the drawing color based on finger location in the header area.
5. **Drawing:** Draws on the canvas based on finger movement.
6. **Erasing:** Erases parts of the canvas using a thicker effect.
7. **Canvas and Header Overlay:** Combines the drawing canvas with the header image.
8. **Display:** Shows the resulting image with the canvas and header.

## Contributing

Feel free to fork this repository and make improvements! We welcome contributions to enhance features, fix bugs, or add functionalities.
