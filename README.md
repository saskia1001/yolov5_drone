## **Real-time object detection of a drone video feed using YOLOv5**

![demo](demo.gif)
![drone_flight](drone_flight.gif)

### **Project Description**
This repository represents a project to perform real-time object detection on custom data on a [Tello](https://www.ryzerobotics.com/de/tello) drone.

To enable object detection, the official [YOLOv5](https://github.com/ultralytics/yolov5) model by [Ultralytics](https://www.ultralytics.com/) was trained on custom data. Be aware that the code base used here might be outdated as the repository of Ultralytics is under constant development. I hlighly recommend to use the official code base of [YOLOv5](https://github.com/ultralytics/yolov5). The code base used by this project is stored in folder `'/yolov5'`.

As subjects to the object detection the two fluffy toys (a duck and a turtle) shown above were chosen to custom train the model. Therefore, 1.500 images were allocated. The images were labelled and processed using [Roboflow](https://roboflow.com/).

This notebook is based on the tutorial by [Roboflow Blog Post](https://blog.roboflow.ai/how-to-train-yolov5-on-a-custom-dataset/). As a template I used their [Colab Notebook](https://colab.research.google.com/drive/1gDZ2xcTOgR39tGGs-EZ6i3RTs16wmzZQ).

The code controlling the drone is based on the code provided in the [tutorial](https://www.murtazahassan.com/courses/drone-programming/) by [Murtaza Hassan](https://www.murtazahassan.com/). Example code for controlling the drone can be found in the folder `'/tello'`.

### **Requirements**
The project is Python 🐍 based. To run the code on your local machine, ensure to include all packages from the `requirements.txt` file.

* Operating Sytem: macOS Big Sur
* SDK drone: [Tello SDK 2.0](https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf)
* Model training: [Google Colab](https://colab.research.google.com/)

In the next step of the project, a Docker image will be provided. For the official Docker image for YOLOv5 please have a look a the [YOLOv5 repository](https://github.com/ultralytics/yolov5)

### **Usage**
**Training & validation on custom data**:\
The training, validation and testing of the model can be found in the notebook called `fluffy_toy_YOLOv5.ipynb`.\
\
**Testing**:\
To run a test of the object detection model on the test file `test.jpg`, run the following in the shell:\
* `python detect.py --weights best.pt --img-size 416 --source test.jpg`\

\
**Run real-time object detection with the drone**:\
To control the drone and run the real-time object detection, run `main.py`. The video feed and the object detection will start after a few seconds in a separate window.\
The drone can be controlled with the following keyboard commands:

* 'e': takoff
* ▶️ (left arrow): move left
* ▶️ (right arrow): move right
* 🔼 (up arrow) : move forwards
* 🔽 (down arrow): move backwards
* 'w': move up
* 's': move down
* 'a': rotate clockwise
* 'd': move anti-clockwise
* 'q': land
* 'z': take picture
* 'x': land the drone and quit program

*Important step before the first usage*: Unfortunately, one pitfall is that the drone needs a wifi connection to enable control via the device. As the model is loaded of PyTorch Hub, make sure to run the program once with an internet connection. Thus, the model can run from the cache when connected to the drone.  

### **Final notes**
The project is in progress and needs and not aligned with the developing code base of the official YOLOv5 repo. The project was my final project at the [SPICED Data Science Bootcamp](https://www.spiced-academy.com/en/program/data-science).