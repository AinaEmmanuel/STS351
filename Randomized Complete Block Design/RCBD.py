# Modules
import pandas as pd
import numpy as np

# Ignore Warnings
import warnings
warnings.filterwarnings("ignore")
data = pd.read_csv('rcbd.csv')
CF = 0

# Number of Treatments
t = data.shape[1]

# Number of Replication
b = data.shape[0]

# Total number of Units
N = t*b

