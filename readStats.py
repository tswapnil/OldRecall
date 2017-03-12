import numpy as np
import datetime
import os
import shutil
from PIL import Image


truth = open('/home/tswapnil/291G/imagenet/ILSVRC2010_test_ground_truth.txt', 'r')

stats = open('stats.txt', 'w')
mat = dict()
for line in truth:
    if line in mat: 
        mat[line] +=1
    else :
        mat[line] = 1

stats.write(str(mat))
print (mat)
