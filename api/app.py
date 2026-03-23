from flask import Flask, request, jsonify
from ultralytics import YOLO
import os

app = Flask(__name__)
model = None

def load_model():
    global model
    model_path = os.getenv('MODEL_PATH', 'best.pt')
    if os.path.exists(model_path):
        model = YOLO(model_path)
        print(f"Model loaded from {model_path}")
    else:
        print("No model found - using default YOLOv8n")
        model = YOLO('yolov8n.pt')

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None
    })

@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    image = request.files['image']
    image.save('/tmp/input.jpg')
    results = model('/tmp/input.jpg', conf=0.25)
    detections = []
    for r in results:
        for box in r.boxes:
            detections.append({
                'confidence': float(box.conf[0]),
                'bbox': box.xyxy[0].tolist(),
                'class': 'drone'
            })
    return jsonify({'detections': detections, 'count': len(detections)})

if __name__ == '__main__':
    load_model()
    app.run(host='0.0.0.0', port=5000)
