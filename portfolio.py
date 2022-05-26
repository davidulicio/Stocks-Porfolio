#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Trejo Cancino
"""

""" 
This script has a Portfolio Class with a profit and price methods for a set of
given stocks.

To run this script you must have all the following packages installed.
If you are using Anaconda you will just need to install the pandas-datareader 
package, using the command conda install pandas-datareader on the Anaconda 
Prompt. 

Additionally, you must be connected to internet since the price of the stocks 
is collected online.

"""

import datetime as dt
import pandas_datareader.data as web
import numpy as np

#%% Class definition
class Portfolio:
    """
    A Portfolio class that has a profit and price method.
    """
    

    def __init__(self, stocks):
        """
        Initial function that receives the stocks to analyze.

        Parameters
        ----------
        stocks : List
            List of strings of the names of the stocks.

         """
        self.stocks = stocks


    def Profit(self, initial_date, final_date):
        """
        Profit function that calculates and returns the profit of the Portfolio
        given two dates.

        Parameters
        ----------
        initial_date : datetime
            Initial date to calculate the profit.
        final_date : datetime
            Final date to calculate the profit.

        Returns
        -------
        profit : float
            Total profit of the Portfolio between those dates.
        self.profit: list of floats
            Profit of each stock between those dates.

        """
        n = len(self.stocks)
        self.profit = np.zeros(n) * np.nan
        print('Profit method')
        print('----------------------------')
        print('Between the selected dates')
        print('Each stock has a profit of: ')
        for i in range(n):
            label = self.stocks[i]
            data = web.DataReader(label,"yahoo", initial_date, final_date)
            i_value = data["Close"].iloc[0]
            f_value = data['Close'].iloc[len(data)-1]
            self.profit[i] = f_value - i_value
            print(label + ' = '+ str(round(self.profit[i], 2)))
        profit = np.sum(self.profit)
        print('The total Portfolio profit is = '+ str(round(profit, 2)))
        print('----------------------------')
        return profit, self.profit

            
    def Price(self, date, stockname):
        """
        Price function that given a stock and date return its price.

        Parameters
        ----------
        date : datetime
            Date of the stock price to be given.
        stockname : string
            Stock symbol (ticker) to analyze.

        Returns
        -------
        self.price: float
            Close Price of the stock at the given date.

        """
        print('Price method')
        print('----------------------------')
        data = web.DataReader(stockname, "yahoo", date, date)
        self.price = data["Close"].iloc[0]
        print('The price of '+ stockname +' on ' + str(date) + ' is = ' +
              str(round(self.price, 2)))
        print('----------------------------')
        return self.price
#%% Example
" Initial variables "
i_year = 2019; i_month = 6; i_day = 3  # Year,Month and day of the initial date
f_year = 2022; f_month = 2; f_day = 20  # Year,Month and day of the final date
initial_date = dt.datetime(i_year, i_month, i_day)
final_date = dt.datetime(f_year, f_month, f_day)
stocks = ['^DJI', 'GC=F', '^IXIC', '^GSPC', 'IBM']  # Example of stocks to include
" Running the Portfolio Class "
tmp = Portfolio(stocks)
# Profit method
profit = tmp.Profit(initial_date, final_date)
# Price method
price = tmp.Price(initial_date, 'IBM')
