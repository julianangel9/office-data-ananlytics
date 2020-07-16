# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:33:41 2020

@author: Cesar
"""
import pandas as pd
xl = pd.ExcelFile("OSSalesData.xlsx")
lines = "="*60
SalesData = xl.parse("Orders")

SalesDataQuarter = SalesData
SalesDataQuarter["Quarter"]= SalesDataQuarter["Order Date"].dt.quarter


quarters = SalesDataQuarter.Quarter.unique()
SubCatData = SalesData[["Sub-Category", "Profit", "Quarter"]]

for quarter in quarters:
    RegSubCatData = SubCatData.loc[SubCatData["Quarter"]==quarter]
    SubCatProfitNoQuarter = RegSubCatData[["Sub-Category", "Profit"]]
    SubCatProfit = RegSubCatData.groupby(by="Sub-Category").sum().sort_values(by="Profit")
    print(lines)
    print(quarter)
    print(SubCatProfit)
