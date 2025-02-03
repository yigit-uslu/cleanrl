# import tensorflow as tf
# import os
# os.environ["CUDA_MODULE_LOADING"] = "LAZY"

# print(tf.config.list_physical_devices('GPU'))
# print(tf.reduce_sum(tf.random.normal([1000, 1000])))
import tensorflow as tf
import os 

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Suppress extra logs
os.environ["CUDA_MODULE_LOADING"] = "LAZY"

print(tf.__version__)  # Check TensorFlow version
# print(tf.config.list_physical_devices('GPU'))  # Check if GPU is recognized

