# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:04:26 2020

@author: Julian
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 12:24:34 2020

@author: Julian
"""
import pandas as pd
xl = pd.ExcelFile("OSSalesData.xlsx")
lines = "="*60
SalesData = xl.parse("Orders")

def SubCat_Profit():
    #shows the sub category of profits 
    SubCatData = SalesData[["Sub-Category","Profit"]]
    SubCatProfit = SubCatData.groupby(by="Sub-Category").sum().sort_values(by="Profit")
    print(SubCatProfit.head(10))



def ProductData():
    #shows 
    ProductData = SalesData[["Product Name", "Profit", "Sales"]]
    print(lines)
    ProdProfSales = ProductData.groupby(by = "Product Name").sum().sort_values(by= "Profit")
    print(ProdProfSales.head(10))




def Regions():
    regions = SalesData.Region.unique()
    SubCatData = SalesData[["Sub-Category","Profit", "Region"]]
    for region in regions:
        RegSubCatData = SubCatData.loc[SubCatData["Region"]==region]
        SubCatProfit = RegSubCatData.groupby(by="Sub-Category").sum().sort_values(by="Profit")
        print(lines)
        print(region)
        print(SubCatProfit)
    

    
    
def Segments():
    segments = SalesData.Segment.unique()
    SubCatData = SalesData[["Sub-Category","Profit", "Segment"]]
    for segment in segments:
        RegSubCatData = SubCatData.loc[SubCatData["Segment"]==segment]
        SubCatProfit = RegSubCatData.groupby(by="Sub-Category").sum().sort_values(by="Profit")
        print(lines)
        print(segment)
        print(SubCatProfit)
        

    
def Product_Data():
    ProductData = SalesData[["Sub-Category","Profit","Product Name"]]
    NegSubCat = ["Tables", "Bookcases", "Supplies"]
    
    for subcat in NegSubCat:
        ProductInfo = ProductData.loc[ProductData["Sub-Category"]==subcat]
        ProdProfit = ProductInfo.groupby(by="Product Name").sum().round().sort_values(by="Profit")
        print(subcat)
        print(ProdProfit)
        print(lines)
        



def SalesData_Year():
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
        

    

def SubCat_Data():
    SubCatData = SalesData[["Sub-Category","Discount"]]
    SubCatDiscount = SubCatData.groupby(by="Sub-Category").mean(). sort_values(by = "Discount", ascending = False)
    print(SubCatDiscount)

def MainMenu():
    print("\n" + "*"*80)
    print("\n Enter (1) to see the Sub-Category Profits" +
          "\n Enter (2) to see all the products in the negative profit Sub-Category" +
          "\n Enter (3) to see all the profits and sales of all products" +
          "\n Enter (4) to see the sub category profits and segment" +
          "\n Enter (5) to see all the profits in the negative Sub Categorys" +
          "\n Enter (6) to see the profits of each Sub Category of eavh year" +
          "\n Enter (7) to see the avergeage discunts with all Sub Categorys" +
          "\n Enter (8) to exit")
    print("\n" + "*"*80)
    choice = input("Pleas enter a number 1 to 8: ")
    if choice =="1":
        SubCat_Profit()
        MainMenu()
    elif choice =="2":
        ProductData()
        MainMenu()
    elif choice =="3":
        Regions()
        MainMenu()
    elif choice =="4":
        Segments()
        MainMenu()
    elif choice =="5":
        Product_Data()
        MainMenu()
    elif choice =="6":
        SalesData_Year()
        MainMenu()
    elif choice =="7":
        SubCat_Data()
        MainMenu()
    elif choice =="8":
        exit()
    else:
        print("Invalid option, please enter a number 1 to 8")
        MainMenu()
print("\nWelcome to the Office Soultions Data Analytics System")
MainMenu()

    

    










#function call