import torch
import os
from torch import nn
import torchvision
from torchvision.models import resnet50, ResNet50_Weights
from PIL import Image
import glob
import torch.nn.functional as F
import matplotlib.pyplot as plt
import numpy as np
import requests


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
# print(leftFileList)
# print(rightFileList)
# fileList.sort()
# print(fileList)
'''
image_list = []
for fname in fileList:
    impath = os.path.join(image_dir, fname)
    im = Image.open(impath)
    new_im = im.copy()
    im.close()
    image_list.append(new_im)
print(len(image_list))
'''
iNet = IrisNet()
# xOut = iNet.forward(x)
# criterion = nn.MultiLabelSoftMarginLoss()
# mLoss = criterion(xOut)
for epoch in range(iNet.epochs):
    pass
    # xOut = iNet.forward(x)
    # print(epoch)
