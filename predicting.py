# importing libraries 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from geopy import distance

# importing data

df = pd.read_csv('/Users/alokkumar/YourCAB/YourCabs_training.csv')
# Dropping target coloumns 
data = df.drop(['Car_cancellation','Cost_of_error'], axis=1) 

target=df[["Car_Cancellation"]]

print(data.info())
