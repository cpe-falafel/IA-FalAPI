import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from cnn_model import create_model
from PIL import Image

DATA_PATH = "../data/"
IMAGE_SIZE = (256, 256)
BATCH_SIZE = 32
EPOCHS = 10
MODEL_SAVE_PATH = "cnn_gore_model.h5"

datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    validation_split=0.2
)

train_data = datagen.flow_from_directory(
    DATA_PATH,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary',
    classes=['images_safe', 'images_gore'],
    subset='training'
)

val_data = datagen.flow_from_directory(
    DATA_PATH,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary',
    classes=['images_safe', 'images_gore'],
    subset='validation'
)

model = create_model(input_shape=(256, 256, 3))

print("Début de l'entraînement...")
history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=EPOCHS
)

print(f"Enregistrement du modèle dans : {MODEL_SAVE_PATH}")
model.save(MODEL_SAVE_PATH)

print("Entraînement terminé.")
