# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 12:34:02 2020

@author: Cesar
"""

import pandas as pd
xl = pd.ExcelFile("OSSalesData.xlsx")
lines= "="*25
SalesData = xl.parse("Orders")
SubCatData = SalesData[["Sub-Category", "Profit"]]
print(lines)
#create functions to group and state sum
SubCatProfit = SubCatData.groupby(by = "Sub-Category").sum().sort_values(by = "Profit")
#print top 10
print(SubCatProfit.head(10))
