import cv2
import supervision as sv
from tqdm import tqdm
from ultralytics import YOLOWorld

class Detect:
    def __init__(self):
        self.model=None
    
        self.box_annotator = sv.BoundingBoxAnnotator()
        self.label_annotator = sv.LabelAnnotator()
        self.cam = None
        self.video_writer =None
        
    def camera(self):
        self.cam = cv2.VideoCapture("box.mp4")
        
    def model_conf(self):
        self.model = YOLOWorld("yolov8x-worldv2")
        self.model.set_classes(["boxes"])
        
    def process(self,frame):
        results = self.model.predict(frame,conf=0.01)[0]
        detections = sv.Detections.from_ultralytics(results).with_nms(threshold=0.1)
        
        labels = [
            f"{class_name}" for class_name in detections['class_name']
        ]
        frame = self.box_annotator.annotate(
            scene=frame,
            detections=detections
        )
        frame = self.label_annotator.annotate(
            scene=frame,
            detections=detections,
            labels=labels
        )
        return frame
    def run(self):
        self.camera()
        self.model_conf()
        while True:
            ret, frame = self.cam.read()
            if not ret:
                break
            frame = self.process(frame)
            cv2.imshow("results",frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        self.cam.release()
        cv2.destroyAllWindows()
if __name__ == "__main__":
    detect= Detect()
    detect.run()
