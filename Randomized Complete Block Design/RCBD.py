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

def rcbd_parameters(data):
    # Calculate Total for each Treatment
    total_each_trt = []
    for col in data.columns:
        total_each_trt.append(round(data[col].sum(),2))

    # Calculate Total for each Block
    total_each_blk = [] # total for each block row
    vals_in_block = [] # value for each block row
    x = 0
    while x < len(data):
        for col in data.columns: # A,B,C...
            vals_in_block.append((data[col][x])) # A0, B0, C0....
        total_each_blk.append(round(sum(vals_in_block),2))# A0+B0+C0...
        vals_in_block=[] # perform reset for A1, B1, C1...
        x+=1

    # Calculate the Correction Factor
    GT = sum(total_each_trt)
    CF = round(GT**2/(t*b), 2)
    
    # SUM OF SQUARES
    # Calculate the Sum of Square Treatment
    square_tot_trt = [val**2 for val in total_each_trt]
    sum_square_tot_trt = sum(square_tot_trt)
    SStrt = round((sum_square_tot_trt/b) - CF, 2)

    # Calculate the Sum of Square Block
    square_tot_blk = [val**2 for val in total_each_blk]
    sum_square_tot_blk = sum(square_tot_blk)
    SSblk = round((sum_square_tot_blk/t) - CF, 2)

    # Calculate the Sum of Square Total
    all_units = []
    for col in data.columns:
        for val in data[col]:
            all_units.append(val)
    square_all_units = [val**2 for val in all_units]
    SStot = round(sum(square_all_units) - CF, 1)

    ## Calculate Sum of Square Error
    SSerr = SStot-SSblk-SStrt
    
    return SStrt, SSblk, SSerr, SStot