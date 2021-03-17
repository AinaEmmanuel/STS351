# Modules
import pandas as pd
import numpy as np

# Ignore Warnings
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv('example.csv')

# Base Variables
N = data.shape[0] * data.shape[1]
k = data.shape[0]
CF = 0


def crd_parameters(data):
    global CF
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

def AnovaTable():
    # Create ANOVA Table
    Anova_Table = pd.DataFrame(columns=['Source of Variation', 'DoF', 'SoS', 'MoS', 'Fcal'])
    
    # Populate SoV with the appropriate parameters
    Anova_Table['Source of Variation'] = ['Treatment', 'Error', 'Total']
    Anova_Table.fillna('-', inplace=True)
    
    # Add the Degree of Freedom
    Anova_Table['DoF'][0] = k-1
    Anova_Table['DoF'][1] = N-k
    Anova_Table['DoF'][2] = N-1
    
    # Populate Sum of Squares with the values gotten in the previous function
    Anova_Table['SoS'] = crd_parameters(data)
    
    # Calculate the Mean of Squares
    for x in range(0,2):
        Anova_Table['MoS'][x] = Anova_Table.SoS[x]/Anova_Table.DoF[x]
    
    # Get Fcalculated
    Anova_Table['Fcal'][0] = Anova_Table['MoS'][0]/Anova_Table['MoS'][1]
    
    return(Anova_Table)

def results():
    trt, err, tot = crd_parameters(data)
    print('=='*30)
    print('\tImportant values For Completely Randomized Design')
    print(
f"""1. SStrt: {trt}
2. SSerr: {err}
3. SStot: {tot}
4. Correction Factor: {CF}
""")

    print('=='*30)
    print('\tANOVA Table For Completely Randomized Design\n')
    print(AnovaTable())

results()