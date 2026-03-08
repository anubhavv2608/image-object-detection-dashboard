Detailed Working of the System

1. User Interface (Taipy Dashboard)

The system provides a graphical user interface developed using the Taipy GUI framework.
The dashboard contains the following components:

Image upload field

Detect Object button

Image preview section

Result display section

This interface allows the user to interact with the machine learning model easily without writing any code.


2. Image Upload

The first step in the system workflow is image upload.

The user selects an image file using the upload component in the dashboard.

Supported formats include:

JPG

PNG

JPEG

Once the image is uploaded, the system stores the file path and displays the image in the dashboard.

Example workflow:

User uploads image
        ↓
Image is loaded using Python Pillow library
        ↓
Image preview is displayed in the GUI

The Pillow (PIL) library is used to read and process the image file.


3. Image Preprocessing

Before sending the image to the machine learning model, preprocessing is required.

The preprocessing steps include:

Resizing the image to 224 × 224 pixels

Converting the image to a NumPy array

Normalizing the pixel values

Expanding the dimensions to match the model input shape

Example process:

Original Image
        ↓
Resize (224 × 224)
        ↓
Convert to NumPy Array
        ↓
Normalize Pixel Values
        ↓
Prepare Input for Model

This step ensures that the image is in the correct format required by the MobileNetV2 model.


4. Machine Learning Model

The project uses the MobileNetV2 deep learning model for object classification.

MobileNetV2 is a lightweight convolutional neural network designed for efficient image recognition tasks.

Key characteristics of MobileNetV2:

Pretrained on ImageNet dataset

Dataset contains over 1 million images

Can recognize 1000 different object categories

Examples of objects the model can detect:

Dog

Cat

Car

Bottle

Laptop

Banana

Phone

Person

The pretrained model is loaded in the program using TensorFlow.

Example pipeline:

Image Input
      ↓
MobileNetV2 Neural Network
      ↓
Feature Extraction
      ↓
Object Classification


5. Model Prediction

Once the image is processed, it is passed to the MobileNetV2 model.

The model analyzes the pixel patterns and produces probability scores for different object classes.

Example output from the model:

Dog → 96%
Cat → 2%
Fox → 1%
Other → 1%

The system selects the highest probability class as the predicted object.

Example final result:

Detected Object: Labrador Retriever (96%)


6. Result Display

After the prediction is generated, the result is displayed on the Taipy dashboard.

The GUI updates dynamically and shows:

Uploaded image preview

Predicted object name

Confidence percentage

Example output displayed in GUI:

Detected Object: Sports Car (91%)

This provides instant feedback to the user.


7. Overall System Workflow

The complete workflow of the system is shown below:

User Uploads Image
        ↓
Image Preprocessing
        ↓
MobileNetV2 Machine Learning Model
        ↓
Object Prediction
        ↓
Result Display on Dashboard

This pipeline demonstrates how machine learning and graphical user interface components can work together to build an interactive object recognition system.

Conclusion

The Image Object Detection Dashboard successfully demonstrates the integration of machine learning with an interactive graphical interface. By using the MobileNetV2 deep learning model, the system can automatically analyze uploaded images and identify the object present in them.

This project highlights the practical application of artificial intelligence techniques in computer vision and object recognition tasks.

✅ You can paste this below the “Working” section in your README or DOC file.

If you want, I can also give you a simple system architecture diagram (like professors expect in reports) that perfectly matches this project.