## Files Included

**blob_detection.py**: Uses blob detection to find blobs 

**canny_edge_detection.py**: Uses Canny edge detection to find shapes

**roboflow.py**: Not yet usable. Will use a trained Roboflow model to detect shapes

**threshold_contours.py**: Original file, uses gaussianBlur, adaptiveThreshold, findContours, and approxPolyDP to find shapes



## Algorithm issues

- lighting and contrast reliance - only detects extremeley light objects on dark baackgrounds and vice versa, not really for intermediates + faulty when there are reflections, shadows, or 3D images but not flat surface

- which algorithm to use - threshold/findcontours, edge detection, Roboflow/ML



## Dobot issues (Will add a link to a new repository with dobot-shape-tracker-overhead in the future)

- Webcam quality (may just be issue with old camera)

- New camera = different frame size

- Camera positioning consistency

- Finish implementing shape sorting, put different shapes into different cups



## Future Actions

- Put a box around the mat = reduce light = remove refelctions/shadows

- Disable camera autofocusing, keep static / play around with settings

- Play around with the blur and thresholding and findcontours?

- Try using Roboflow/YOLO

- Blob keypoints --> contours?

- Background subtraction technique