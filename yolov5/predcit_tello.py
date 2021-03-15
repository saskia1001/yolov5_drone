from PIL import Image
from yolov5 import YOLOv5

# set model params
model_path = "/Users/saskia/Dropbox/ELLA/yolov5_fluffy_tello/yolov5/weights/best.pt" # it automatically downloads yolov5s model to given path
device = "cpu" # or "cuda"

# init yolov5 model
yolov5 = YOLOv5(model_path, device)

# load images
image1 = Image.open("/Users/saskia/Dropbox/ELLA/yolov5_fluffy_tello/ella_and_fredi.jpg")
# image2 = Image.open("yolov5/data/images/zidane.jpg")

# perform inference
results = yolov5.predict(image1)

# perform inference with higher input size
results = yolov5.predict(image1, size=1280)

# perform inference with test time augmentation
results = yolov5.predict(image1, augment=True)

# perform inference on multiple images
# results = yolov5.predict([image1, image2], size=1280, augment=True)