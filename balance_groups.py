import torch
import torch.nn as nn
import numpy as np
import pandas as pd
import os
import torch.nn.functional as F
import tqdm
import pickle
from collections import defaultdict

with open('0score.pkl', 'rb') as f:
    scores = pickle.load(f)

scores.sort(key = lambda x:x[1])

all_0 = []
all_1 = []

counter_0 = 0
counter_1 = 0

for i, j, k, l in scores:
    if k == 0:
        all_0.append(i)
    if k == 1:
        all_1.append(i)

l0 = len(all_0)
l1 = len(all_1)

all_ind = all_0[:3400] + all_1[:800]

with open('rank_20.pkl', 'wb') as f:
    pickle.dump(all_ind, f)
