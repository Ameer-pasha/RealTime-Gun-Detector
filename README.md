# Gun Detection System

A real-time gun detection system using OpenCV and Haar Cascade classifiers for security monitoring applications.

## Features

- Real-time gun detection from webcam feed
- Automatic screenshot capture when guns are detected
- JSON logging of all detections with timestamps and coordinates
- Visual bounding boxes around detected objects
- Configurable detection parameters

## Requirements

- Python 3.7+
- Webcam/Camera device
- cascade.xml file (Haar cascade classifier for gun detection)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd gun-detection-system
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Download the cascade.xml file:
   - The training data was sourced from: https://drive.google.com/file/d/1Ndr_HFhxHB8mJ_uysdasXgfAKSQ2is4q/view
   - Place the `cascade.xml` file in the project root directory

## Usage

1. Ensure your camera is connected and working
2. Run the detection system:
```bash
python gun_detection.py
```

3. The system will:
   - Open a window showing the camera feed
   - Display timestamp overlay
   - Detect and highlight guns with red rectangles
   - Save screenshots when guns are detected
   - Log detection data to `detections.json`

4. Press 'q' to quit the application

## Output Files

- **Screenshots**: `detection_YYYYMMDD_HHMMSS.jpg` - Saved when guns are detected
- **detections.json**: Contains detection metadata including:
  - Detection ID
  - Timestamp
  - Number of guns detected
  - Screenshot filename
  - Bounding box coordinates

## Configuration

You can adjust detection sensitivity by modifying these parameters in the code:

```python
guns = gun_cascade.detectMultiScale(
    gray, 
    scaleFactor=1.3,    # How much the image size is reduced at each scale
    minNeighbors=20,    # How many neighbors each candidate rectangle should retain
    minSize=(100, 100)  # Minimum possible gun size
)
```

## System Requirements

- Camera resolution: Automatically resized to 500px width
- Minimum detection size: 100x100 pixels
- Supported formats: All OpenCV supported video formats

## Troubleshooting

**Error: cascade.xml file not found!**
- Ensure the cascade.xml file is in the project root directory
- Download from the provided Google Drive link

**Error: Could not open camera!**
- Check camera permissions
- Ensure no other applications are using the camera
- Try changing camera index in `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)`

**Poor detection accuracy:**
- Adjust `scaleFactor`, `minNeighbors`, and `minSize` parameters
- Ensure good lighting conditions
- Keep objects at appropriate distance from camera

## Legal Notice

This software is intended for educational and authorized security purposes only. Users are responsible for complying with all applicable laws and regulations regarding surveillance and privacy in their jurisdiction.

## License

This project is for educational purposes. Please ensure you have proper authorization before deploying in any security context.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Support

For issues and questions, please check the troubleshooting section or create an issue in the repository.