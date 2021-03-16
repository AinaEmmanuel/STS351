# Modules
import pandas as pd
import numpy as np

data = pd.read_csv('/home/emmanuel/Emmanuel/Work/Experiment Design/CRD.csv')

# Base Variables
N = data.shape[0] * data.shape[1]
k = data.shape[0]

def crd_parameters(data):
    # Calculate Grand Total
    total_each_trt = []
    for col in data.columns:
        total_each_trt.append(data[col].sum())
        
    # Calculate the Correction Factor
    GT = sum(total_each_trt)
    CF = round(GT**2/N, 1)