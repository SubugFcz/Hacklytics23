import sys
import pandas as pd
import os
import numpy as np
import functions as fn
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print(fn.superFunction('04-02-2021', '15-05-2021'))
    d = fn.superFunction('04-02-2021', '15-05-2021')
    print(d.values.tolist())