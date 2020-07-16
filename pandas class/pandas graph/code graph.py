# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 10:56:38 2020

@author: Julian
"""
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

xl = pd.ExcelFile("OSSalesData.xlsx")
SalesData = xl.parse("Orders")
SalesDataMonth = SalesData
SalesDataMonth["Month"] = SalesDataMonth["Order Date"].dt.month
MonthlySales = SalesDataMonth[["Month", "Sales"]]
MonthlySalesSum = MonthlySales.groupby("Month").sum()
print(MonthlySalesSum)

MonthlySalesSum = MonthlySalesSum.reset_index()

plt.figure(figsize=(8,8))
plt.title("Monthly Sales Percentages")
plt.pie(MonthlySalesSum.Sales, labels = MonthlySalesSum.Month,autopct = "%1.1f%%")
plt.show()

barchart1 = sns.barplot(x= "Month", y="Sales", data = MonthlySalesSum)
barchart1.set_title("Sales by Month")