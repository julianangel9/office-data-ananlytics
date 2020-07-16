# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:04:26 2020

@author: Julian
"""
#position arguments
def make_shirt (size,text):
    print("You have ordered a shirt size of " + size + "with the writing" + text)
make_shirt("Large","Hi")

def make_shirt(size,text):
    print("You have ordered a shirt size of " + size + "with the writing " + text)
    
make_shirt(size= "Large" , text = "addidas")
    
    
def InviteGuests (guest1,guest2,guest3):
    print("Welcome " +guest1 +", " + guest2+ ", and " +guest3)
InviteGuests ('Julian','Bob','Rick')

def CalcSalary(HourlyWage, HoursWorked):
    print("You make " , HourlyWage, "per hour, and have worked", HoursWorked, "hours, so youn have made $" ,(HourlyWage* HoursWorked))
CalcSalary(15.50,40)

def HelloWorld():
    print ("Hello")
HelloWorld()




#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 12:24:34 2020

@author: julian
"""
import pandas as pd
xl = pd.ExcelFile("OSSalesData.xlsx")
lines = "="*60
SalesData = xl.parse("Orders")

def SubCatProfit():
    SubCatData = SalesData[["Sub-Category","Profit"]]
    SubCatProfit = SubCatData.groupby(by="Sub-Category").sum().sort_values(by="Profit")
    print(SubCatProfit.head(10))

SubCatProfit()

def ProductData():
    ProductData = SalesData[["Product Name", "Profit", "Sales"]]
    print(lines)
    ProdProfSales = ProductData.groupby(by = "Product Name").sum().sort_values(by= "Profit")
    print(ProdProfSales.head(10))
ProductData()



def SubCat_Region():
    regions = SalesData.Region.unique()
    SubCatData = SalesData[["Sub-Category","Profit", "Region"]]
    for region in regions:
        RegSubCatData = SubCatData.loc[SubCatData["Region"]==region]
        SubCatProfit = RegSubCatData.groupby(by="Sub-Category").sum().sort_values(by="Profit")
        print(lines)
        print(region)
        print(SubCatProfit)
    
SubCat_Region()
    
    
def Segments():
    segments = SalesData.Segment.unique()
    SubCatData = SalesData[["Sub-Category","Profit", "Segment"]]
    for segment in segments:
        RegSubCatData = SubCatData.loc[SubCatData["Segment"]==segment]
        SubCatProfit = RegSubCatData.groupby(by="Sub-Category").sum().sort_values(by="Profit")
        print(lines)
        print(segment)
        print(SubCatProfit)
        
Segments()
    
def ProductData():
    ProductData = SalesData[["Sub-Category","Profit","Product Name"]]
    NegSubCat = ["Tables", "Bookcases", "Supplies"]
    
    for subcat in NegSubCat:
        ProductInfo = ProductData.loc[ProductData["Sub-Category"]==subcat]
        ProdProfit = ProductInfo.groupby(by="Product Name").sum().round().sort_values(by="Profit")
        print(subcat)
        print(ProdProfit)
        print(lines)
        
ProductData()


def Sales_DataYear():
    SalesDataYear = SalesData
    SalesDataYear["Year"]= SalesDataYear["Order Date"].dt.year
    
    
    years = SalesDataYear.Year.unique()
    print(years)
    SubCatData = SalesDataYear[["Sub-Category","Profit", "Year"]]
    for year in years:
        SubCatDataByYear = SubCatData.loc[SubCatData["Year"]==year]
        SubCatProfitNoYear = SubCatDataByYear [["Sub-Category", "Profit"]]
        SubCatProfit = SubCatProfitNoYear.groupby(by="Sub-Category").sum().sort_values(by="Profit")
        print(lines)
        print(year)
        print(SubCatProfit)
        
Sales_DataYear()
    

def Sub_CatData():
    SubCatData = SalesData[["Sub-Category","Discount"]]
    SubCatDiscount = SubCatData.groupby(by="Sub-Category").mean(). sort_values(by = "Discount", ascending = False)
    print(SubCatDiscount)


Sub_CatData













#function call