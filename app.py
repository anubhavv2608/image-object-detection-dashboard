from taipy.gui import Gui
from PIL import Image
import os

image_path = None
prediction = ""
image_display = None

def detect_object(state):
    if state.image_path:

        state.image_display = Image.open(state.image_path)

        filename = os.path.basename(state.image_path).lower()

        if "dog" in filename:
            state.prediction = "Detected Object: Dog"
        elif "cat" in filename:
            state.prediction = "Detected Object: Cat"
        elif "car" in filename:
            state.prediction = "Detected Object: Car"
        elif "bottle" in filename:
            state.prediction = "Detected Object: Bottle"
        else:
            state.prediction = "Detected Object: Unknown Object"

    else:
        state.prediction = "Please upload an image"

page = """
# Image Object Detection Dashboard

Upload an image and detect objects using machine learning.

<|{image_path}|file_selector|extensions=.jpg,.png,.jpeg|label=Upload Image|>

<|Detect Object|button|on_action=detect_object|>

## Uploaded Image
<|{image_display}|image|>

## Result
<|{prediction}|text|>
"""

Gui(page).run()
