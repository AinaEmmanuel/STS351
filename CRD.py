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

    # Calculate the Sum of Square Treatment
    square_tot_trt = [val**2 for val in total_each_trt]
    sum_square_tot_trt = sum(square_tot_trt)
    SStrt = round((sum_square_tot_trt/k) - CF, 1)
    
    # Calculate the Sum of Square Total
    all_units = []
    for col in data.columns:
        for val in data[col]:
            all_units.append(val)
    square_all_units = [val**2 for val in all_units]
    SStot = round(sum(square_all_units) - CF, 1)

    # Calculate the Sum of Square Error
    SSerr = round(SStot -SStrt, 1)

    return(SStrt, SSerr, SStot)

print(crd_parameters(data))