from taipy.gui import Gui
from PIL import Image
import numpy as np
import tensorflow as tf

# Load MobileNet model once
model = tf.keras.applications.MobileNetV2(weights="imagenet")

image_path = None
image_display = None
prediction = ""

def detect_object(state):

    if state.image_path is None:
        state.prediction = "Please upload an image."
        return

    img = Image.open(state.image_path)
    state.image_display = img

    img = img.resize((224, 224))
    img = np.array(img)

    img = np.expand_dims(img, axis=0)
    img = tf.keras.applications.mobilenet_v2.preprocess_input(img)

    preds = model.predict(img)

    decoded = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=1)[0]

    label = decoded[0][1]
    confidence = decoded[0][2]

    state.prediction = f"Detected Object: {label} ({round(confidence*100,2)}%)"

page = """
# Image Object Detection Dashboard

Upload an image and detect objects using Machine Learning.

<|{image_path}|file_selector|extensions=.jpg,.png,.jpeg|label=Upload Image|>

<|Detect Object|button|on_action=detect_object|>

## Uploaded Image
<|{image_display}|image|>

## Result
<|{prediction}|text|>
"""

Gui(page).run()
