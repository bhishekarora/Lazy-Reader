# Hand Gesture Controlled Scrolling

This project allows you to scroll a webpage up and down by detecting the vertical movement of your index finger using your webcam. It utilizes MediaPipe for hand tracking and pyautogui for simulating scroll events.

#![Picture](https://github.com/bhishekarora/Lazy-Reader/blob/main/1.png.jpg) { height =200px width=250px}

## Requirements

- Python 3.x
- OpenCV
- MediaPipe
- PyAutoGUI
- NumPy

## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```sh
    python hand_gesture_scroll.py
    ```

2. The script will open a window displaying the video feed from your webcam. Move your index finger up or down in front of the camera to scroll the page.

3. Press the 'q' key to quit the application.

## How It Works

- The script captures video frames from your webcam and processes them using MediaPipe's hand tracking solution.
- It detects the position of the index finger and calculates the vertical movement.
- If the movement exceeds a threshold and the cooldown period has passed, it simulates a scroll event using pyautogui.
- A 3-second cooldown period is implemented to allow the finger to return to a neutral position after scrolling.

## Troubleshooting

- Ensure that your webcam is properly connected and working.
- Make sure you have installed all the required packages.
- Adjust the sensitivity and thresholds if the scrolling is too sensitive or not responsive enough.

## Contributing

If you have any suggestions or improvements, feel free to create a pull request or open an issue.

## License

This project is licensed under the MIT License.
