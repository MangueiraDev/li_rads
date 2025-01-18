from tensorflow.keras.models import load_model
import numpy as np

model = load_model('unet_model.h5')
image = np.expand_dims(normalized_image, axis=0)
segmented_image = model.predict(image)[0]