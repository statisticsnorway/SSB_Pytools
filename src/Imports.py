import pandas as pd
import numpy as np
import os
import statsmodels.api as sm
import matplotlib.pyplot as plt
import datetime
from datetime import datetime
import seaborn as sns
import math
import time

from pandas.api.types import is_string_dtype, is_numeric_dtype, is_categorical_dtype

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import validation_curve
from sklearn import metrics
from sklearn.externals import joblib
import pickle
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score



pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

timestr = time.strftime("%Y%m%d")