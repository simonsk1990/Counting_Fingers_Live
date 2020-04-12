import cv2
import numpy as np
from sklearn.metrics import pairwise


#initilizng parameters
backround = None
accumelated_weight = 0.5
roi_top = 20
roi_bottom = 300
roi_left=300
roi_right=600

def calc_accum_avg(frame,accumulated,weight):
    global backround
    if backround is None:
        backround = frame.copy().astype('float')
        return None
    cv2.accumulateWeighted(frame,backround,accumelated_weight)