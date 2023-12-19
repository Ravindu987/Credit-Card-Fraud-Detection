import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("./model2.hdf5", compile=False)

model.compile(loss="binary_crossentropy", optimizer="adam", metrics="accuracy")


file = open("weights.txt", "w")

# Print weights of each layer
for layer in model.layers:
    file.write(layer.name)
    file.write("\n")
    layer_weights = layer.get_weights()
    # layer_weights_np = [np.around(w, decimals=5) for w in layer_weights]
    np.set_printoptions(suppress=True, precision=5)
    file.write(str(layer_weights))
    file.write("\n")
    file.write("==============================================\n")
