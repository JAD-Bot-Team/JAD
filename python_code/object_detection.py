import cv2
import tensorflow as tf

# Load the pre-trained object detection model
model = tf.keras.applications.MobileNetV2(weights='imagenet')

def perform_object_detection(image_path):
    # Load and preprocess the image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = tf.image.resize(image, (224, 224))
    image = tf.expand_dims(image, axis=0)
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)

    # Perform object detection
    predictions = model.predict(image)
    top_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=5)[0]

    # Extract relevant information from predictions
    detected_objects = []
    for prediction in top_predictions:
        class_id, class_name, probability = prediction
        detected_objects.append({'class_id': class_id, 'name': class_name, 'probability': probability})

    return detected_objects
