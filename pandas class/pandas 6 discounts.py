# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:33:41 2020

@author: Cesar
"""
import pandas as pd
xl = pd.ExcelFile("OSSalesData.xlsx")
lines = "="*60
SalesData = xl.parse("Orders")

SubCatData = SalesData[["Sub-Category", "Disocunt"]]
SubCatDiscount = SubCatData.groupby(by="Sub-Category").mean().sort_value(by="Discounts",ascending)
print(SubCatDiscounts)
    
