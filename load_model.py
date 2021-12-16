import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"

import tensorflow_hub as hub
import tensorflow as tf
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


def load_image(image_path):
    image = tf.image.decode_image(tf.io.read_file(image_path))
    # If PNG, remove the alpha channel. The model only supports
    # images with 3 color channels.
    if image.shape[-1] == 4:
        image = image[...,:-1]
    hr_size = (tf.convert_to_tensor(image.shape[:-1]) // 4) * 4
    image = tf.image.crop_to_bounding_box(image, 0, 0, hr_size[0], hr_size[1])
    return tf.expand_dims(image, 0)

def save_image(image, filename):
    if not isinstance(image, Image.Image):
        image = tf.clip_by_value(image, 0, 255)
        image = Image.fromarray(tf.cast(image, tf.uint8).numpy())
    image.save("%s.jpg" % filename)
    print("Saved as %s.jpg" % filename)

def show_image(image, filename):
    """
        Saves unscaled Tensor Images.
        Args:
        image: 3D image tensor. [height, width, channels]
        filename: Name of the file to save.
    """
    print('show image')
    image = np.asarray(image)
    image = tf.clip_by_value(image, 0, 255)
    image = Image.fromarray(tf.cast(image, tf.uint8).numpy())
    plt.imshow(image)
    plt.axis("off")
    plt.title(filename)

# if tf.test.gpu_device_name():
#     print('GPU found')
# else:
#     print("No GPU found")

def run_model(upload_path, save_path):
    save_path, extension = os.path.splitext(save_path)
    model = hub.load("esrgan-tf2_1")
    # To add an extra dimension for batch, use tf.expand_dims()
    # Low Resolution Image of shape [batch_size, height, width, 3]
    low_resolution_image = load_image(upload_path)
    low_resolution_image = tf.cast(low_resolution_image, tf.float32)
    super_resolution = model(low_resolution_image)  # Perform Super Resolution here
    save_image(tf.squeeze(super_resolution), save_path)
    # show_image(tf.squeeze(super_resolution), 'tes1')