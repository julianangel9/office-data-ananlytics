# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 10:56:38 2020

@author: Cesar
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

xl = pd.ExcelFile("OSSalesData.xlsx")
SalesData = xl.parse("Orders")
SalesDataMonth = SalesData
SalesDataMonth["Month"] = SalesDataMonth["Order Date"].dt.month

