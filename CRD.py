# Modules
import pandas as pd
import numpy as np

data = pd.read_csv('/home/emmanuel/Emmanuel/Work/Experiment Design/CRD.csv')

# Base Variables
N = data.shape[0] * data.shape[1]
k = data.shape[0]