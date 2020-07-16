# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 12:46:36 2020

@author: Cesar
"""

import pandas as pd
xl = pd.ExcelFile("OSSalesData.xlsx")
lines = "="*25
SalesData = xl.parse("Orders")
ProductData = SalesData[["ProductName", "Profit", "Sales"]]
print(lines)
#fucntions to group by sum
ProdProfSales = ProductData.groupby(by= "ProductName").sum().sort_values(by = "Profit")
#print top 10
print(ProdProfSales.head(10))