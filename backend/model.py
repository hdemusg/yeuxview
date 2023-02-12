
import torch
import os
from torch import nn
import torchvision
from torchvision.models import resnet50, ResNet50_Weights
from sklearn.model_selection import train_test_split
from torchvision import transforms
import pandas as pd
from PIL import Image
import glob
import torch.nn.functional as F
import matplotlib.pyplot as plt
import numpy as np
import requests
import pandas as pd


class IrisNet(nn.Module):

    def __init__(self):
        super(IrisNet, self).__init__()
        self.epochs = 5
        self.model = resnet50(weights = ResNet50_Weights.DEFAULT)
        self.model.fc = nn.Sequential(
            nn.Dropout(0.5),
            nn.Linear(2048, 1024),
            nn.Linear(1024, 256),
            nn.Linear(256, 8)
        )

    def forward(self, x):
        resx = self.model(x)
        return x

# print(os.getcwd())
image_dir = os.getcwd() + "/image_files"
# print(image_dir)
fileList = os.listdir(image_dir)
leftFileList = []
rightFileList = []
for fname in fileList:
    if "_left" in fname:
        leftFileList.append(fname)
    if "_right" in fname:
        rightFileList.append(fname)
leftFileList.sort()
rightFileList.sort()
leftIds = []
leftIdNums = []
rightIds = []
rightIdNums = []
for elem in leftFileList:
    id = int(elem.split("_")[0])
    leftIds.append((id, elem))
    leftIdNums.append(id)
for elem in rightFileList:
    id = int(elem.split("_")[0])
    rightIds.append((id, elem))
    rightIdNums.append(id)
leftIds.sort()
leftIdNums.sort()
rightIds.sort()
rightIdNums.sort()
# print(len(leftIdNums))
# print(len(rightIdNums))
diff1 = list(set(leftIdNums) - set(rightIdNums))
diff2 = list(set(rightIdNums) - set(leftIdNums))
# print(diff1)
# print(diff2)
diff3 = diff1 + diff2
diff = list(set(diff3))
diff.sort()
# print(len(diff))
for val1 in leftIds[:]:
    if val1[0] in diff:
        leftIds.remove(val1)
for val2 in rightIds[:]:
    if val2[0] in diff:
        rightIds.remove(val2)
leftIds.sort()
rightIds.sort()
# print(leftIds)
# print(rightIds)
# print(len(leftIds))
# print(len(rightIds))
leftTest = []
rightTest = []
for elem in rightIds:
    rightTest.append(elem[0])
for elem in leftIds:
    leftTest.append(elem[0])

rightTest.sort()
leftTest.sort()

# print(leftTest == rightTest)
# print(rightTest)
# for elem in leftIdNums:
    # if elem not in leftIdNums:
        # print(elem)

# fileList.sort()
# print(fileList)
df = pd.read_csv (os.getcwd() + "/full_df.csv")
# print(df)



left_image_list = []
for id, fname in leftIds:
    impath = os.path.join(image_dir, fname)
    im = Image.open(impath)
    new_im = im.copy()
    im.close()
    left_image_list.append(new_im)

right_image_list = []
for id, fname in rightIds:
    impath = os.path.join(image_dir, fname)
    im = Image.open(impath)
    new_im = im.copy()
    im.close()
    right_image_list.append(new_im)

# print(left_image_list[0:5])
# print(right_image_list[0:5])

img_list_combined = []
for i in range(len(left_image_list)):
    img_list_combined.append((leftTest[i], left_image_list[i], right_image_list[i]))
# print(len(img_list_combined))
# print(img_list_combined[0:4])


ground_truth = []
for id in leftTest:
    val = df[df['ID'] == id]['target']
    # print(val.values)
    left_val = val.values[1]
    right_val = val.values[0]
    left_val = left_val.replace("[", "")
    left_val = left_val.replace("]", "")
    left_val = left_val.strip().split(",")
    left_val = [int(x) for x in left_val]
    right_val = right_val.replace("[", "")
    right_val = right_val.replace("]", "")
    right_val = right_val.strip().split(",")
    right_val = [int(x) for x in right_val]
    # print(left_val)
    # print(right_val)
    ground_truth.append((left_val, right_val))
# print(len(ground_truth))
# print(ground_truth)

X_train, X_test, y_train, y_test = train_test_split(img_list_combined, ground_truth, test_size=0.2, random_state=1)
X_train, X_val, y_train, y_val = train_test_split(img_list_combined, ground_truth, test_size=0.125, random_state=1)

print(len(X_train), len(X_test), len(X_val))
print(len(y_train), len(y_test), len(y_val))

iNet = IrisNet()
tensor_conversion = transforms.ToTensor()
# xOut = iNet.forward(x)
# criterion = nn.MultiLabelSoftMarginLoss()
# mLoss = criterion(xOut)
new_X_train = []
for i in range(len(X_train)):
    img1 = X_train[i][1]
    img2 = X_train[i][2]
    X1 = tensor_conversion(img1).numpy()
    X2 = tensor_conversion(img2).numpy()
    new_X_train.append([X1, X2])
new_Y_train = []
for j in range(len(y_train)):
    t1 = y_train[j][0]
    t2 = y_train[j][1]
    # print(t1)
    # print(t2)
    Y1 = np.array(t1)
    Y2 = np.array(t2)
    new_Y_train.append([Y1, Y2])
new_X_train = torch.as_tensor(np.array(new_X_train))
new_Y_train = torch.as_tensor(np.array(new_Y_train))
for epoch in range(iNet.epochs):
    xOut = iNet.forward(new_X_train)
    criterion = nn.MultiLabelSoftMarginLoss()
    loss = criterion(new_X_train, new_Y_train)
    print("Epoch:" + epoch)
    print("Loss:" + loss)
path = os.getcwd() + "/trained_eye_model.pth"
torch.save(iNet.state_dict(), path)