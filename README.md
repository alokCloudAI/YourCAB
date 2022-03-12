# YourCAB

Problem to Tackled to improve customer service for CAB company.
Problem of interest is booking cancellation by the company due to unavailability of a car.
The challenge is that cancellations can occur very close to trip start time, thereby causing passenger inconvenience.

# Solution

The goal of the competition is to create a predictive model for classifying new bookings as to whether they will eventually gets cancelled due to car unavailability. 

# import libraries 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from geopy import distance  # Need to install geopy :- pip install geopy