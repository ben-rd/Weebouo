from tqdm import tqdm
from PIL import Image
import numpy as np
import os
import random

def flip(img):
    return img.transpose(Image.FLIP_LEFT_RIGHT)

def rotate(img):
    return img.rotate(90)

def addnoise(img):
    img = img.resize((100,100),Image.LANCZOS)
    img = img.resize((200,200),Image.LANCZOS)
    return img

dir_path = r"C:\Users\Jun Sern\Desktop\ROV Project\Python_Work\16072019"

ext = ('png', 'PNG', 'jpg', 'JPG', 'jpeg', 'JPEG', 'tif', 'TIF', 'tiff', 'TIFF')

lined = []
unlined = []

for root, dirs, files in os.walk(os.path.join(dir_path, 'lined')):
    for f in files:
        if f.endswith(ext):
            lined.append(os.path.join(root, f))
for root, dirs, files in os.walk(os.path.join(dir_path, 'unlined')):
    for f in files:
        if f.endswith(ext):
            unlined.append(os.path.join(root, f))

random.shuffle(lined)
random.shuffle(unlined)

training_dataset  = []
training_labels  = []
testing_dataset  = []
testing_labels  = []

for f in tqdm(lined[:300]):
    im = Image.open(f).convert('RGBA').convert('RGB')
    ima = [im, flip(im)]

    for i in range(0,2):
        ima.append(rotate(ima[i]))

    for i in range(0,4):
        ima.append(addnoise(ima[i]))

    for i in range(0,8):
        training_dataset.append(np.array(ima[i], dtype=np.float32) / 255)
        training_labels.append(1)

for f in tqdm(unlined[:300]):
    im = Image.open(f).convert('RGBA').convert('RGB')
    ima = [im, flip(im)]

    for i in range(0,2):
        ima.append(rotate(ima[i]))

    for i in range(0,4):
        ima.append(addnoise(ima[i]))

    for i in range(0,8):
        training_dataset.append(np.array(ima[i], dtype=np.float32) / 255)
        training_labels.append(0)

for f in tqdm(lined[300:350]):
    im = Image.open(f).convert('RGBA').convert('RGB')
    ima = [im, flip(im)]

    for i in range(0,2):
        ima.append(rotate(ima[i]))

    for i in range(0,4):
        ima.append(addnoise(ima[i]))

    for i in range(0,8):
        testing_dataset.append(np.array(ima[i], dtype=np.float32) / 255)
        testing_labels.append(1)

for f in tqdm(unlined[300:350]):
    im = Image.open(f).convert('RGBA').convert('RGB')
    ima = [im, flip(im)]

    for i in range(0,2):
        ima.append(rotate(ima[i]))

    for i in range(0,4):
        ima.append(addnoise(ima[i]))

    for i in range(0,8):
        testing_dataset.append(np.array(ima[i], dtype=np.float32) / 255)
        testing_labels.append(0)

training_dataset = np.asarray(training_dataset)
training_labels = np.asarray(training_labels)
testing_dataset = np.asarray(testing_dataset)
testing_labels = np.asarray(testing_labels)

print(training_dataset.shape)
print(training_labels.shape)
print(testing_dataset.shape)
print(testing_labels.shape)

np.save('train_dataset_2classes', training_dataset)
np.save('train_labelset_2classes', training_labels)
np.save('test_dataset_2classes', testing_dataset)
np.save('test_labelset_2classes', testing_labels)
