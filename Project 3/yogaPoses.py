from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

print('\n\n CORRECT YOUR YOGA POSES')
print(" Give the image of your yoga pose to cheak whether your pose is correctly matched or you are making correct pose or not.\n")

# Load the model
model = load_model('keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


# Replace this with the path to your image
image = Image.open('pose/plank.jpg')


#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)

image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
image_array = np.asarray(image)


# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1


# Load the image into the array
data[0] = normalized_image_array

# run the inference
prediction = model.predict(data)


# Open labels file to read it and store it in content in str form
file=open("labels.txt")
content =file.read()

# Take the index of maximum values along an axis and convert it to string type
s1 = str(np.argmax(prediction[0],axis=0))

# Find out the next index after maximum value index in form of string type
s2 = str(int(s1)+1)          



# Find the indices in content of  maximum value string and next of maximum value string
i = content.index(s1)
i = i+2
j = content.index(s2)


print(' Your yoga pose is: '+content[i:j])


# closing the file 
file.close()

# show the given image
image.show()

# printing prediction list
print("The List of prediction of every Pose:")
print(prediction)
