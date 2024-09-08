# HandGestures1D

HandGestures1D is a Python project that uses OpenCV and MediaPipe to detect hand gestures and control keyboard inputs based on the detected gestures.

## Table of Contents
- Introduction
- Features
- Installation
- Usage
- Contributing
- License
- Acknowledgements

## Introduction
This project leverages computer vision techniques to detect hand gestures in real-time using a webcam. The detected gestures are then used to simulate keyboard inputs, making it possible to control applications without touching the keyboard.

## Features
- Real-time hand gesture detection
- Control keyboard inputs based on gestures
- Easy to set up and use

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/mohammad-azam22/HandGestures1D.git
   cd HandGestures1D
   ```
2. Create a virtual environment and activate it:
  `python -m venv venv`
  source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the required packages:
   `pip install -r requirements.txt`
## Usage
  1. Ensure your webcam is connected.
  2. Run the script:
    `python hand_gestures.py`
  3. Use hand gestures to control the keyboard inputs:
    - Move your thumb above your little finger to simulate a “left” key press (Shown in figure).
    - Move your thumb below your little finger to simulate a “right” key press (Shown in figure).
  
  ![Left Key](https://github.com/user-attachments/assets/4dadacc7-7dde-4584-8ccc-cd63a793d515)
  ![No Key](https://github.com/user-attachments/assets/56f09d6f-37da-49c5-897b-93fc1ecf627b)
  ![Right Key](https://github.com/user-attachments/assets/c198d5b6-15c1-45a0-8ce2-6b524078828b)

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the Apache 2.0 License. See the LICENSE file for details.

## Acknowledgements
  - OpenCV
  - MediaPipe
  - PyAutoGUI
