# Real-time object detection of a drone video feed using YOLOv5

![demo](demo.gif)

## Project Description
This repository represents a project to perform real-time object detection on custom data on a [Tello](https://www.ryzerobotics.com/de/tello) drone. It was my final project at the [SPICED Data Science Bootcamp](https://www.spiced-academy.com/en/program/data-science).

To enable object detection, the official [YOLOv5](https://github.com/ultralytics/yolov5) model by [Ultralytics](https://www.ultralytics.com/) was trained on custom data. Be aware that the code base used here might be outdated as the repository of Ultralytics is under constant development. I hlighly recommend to use the official code base of [YOLOv5](https://github.com/ultralytics/yolov5).

As subjects to the object detection the two fluffy toys (a duck and a turtle) shown above were chosen to custom train the model. Therefore, 1.500 images were allocated. The images were labelled and processed using [Roboflow](https://roboflow.com/).

The training, validation and testing of the model can be found in the notebook called `fluffy_toy_YOLOv5.ipynb`. This notebook is based on the tutorial by [Roboflow Blog Post](https://blog.roboflow.ai/how-to-train-yolov5-on-a-custom-dataset/). As a template I used their [Colab Notebook](https://colab.research.google.com/drive/1gDZ2xcTOgR39tGGs-EZ6i3RTs16wmzZQ).

The code controlling the drone is based on the code provided in the [tutorial](https://www.murtazahassan.com/courses/drone-programming/) by [Murtaza Hassan](https://www.murtazahassan.com/).

## Installations
