import torch
from torch import nn
import torchvision
from torchvision.models import resnet50, ResNet50_Weights
import torch.nn.functional as F
import matplotlib.pyplot as plt
import numpy as np
import requests


class IrisNet(nn.Module):

    def __init__(self, h, w):
        super(IrisNet, self).__init__()
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


iNet = IrisNet(250, 250)
xOut = iNet.forward(x)
criterion = nn.MultiLabelSoftMarginLoss()
mLoss = criterion(xOut)

# print(iNet.model)