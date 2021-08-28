"""
Author: Tran Dinh Hoang
Date: 07/08/2021
Program: Exercise_01_page_158.py
Problem:

    1.  Give three examples of real-world objects that behave like a dictionary.

* * * * * ============================================================================================= * * * * *

Solution:
    Result:
        Date: 2019-02-18
        Close price: 148.0

        Date: 2019-02-19
        Close price: 149.0 

        Date: 2019-02-20
        Close price: 150.0

"""

price_history = [
    {"ticker": "AAPL", "close price": 148.00, "daily high": 152.0, "daily low": 147.0, "volume": 2000000, "date": "2019-02-18"},
    {"ticker": "AAPL", "close price": 149.00, "daily high": 150.0, "daily low": 146.0, "volume": 2000000, "date": "2019-02-19"},
    {"ticker": "AAPL", "close price": 150.00, "daily high": 151.0, "daily low": 149.0, "volume": 2000000, "date": "2019-02-20"}]

for dict in price_history:
    print("Date: %s" % dict['date'])
    print("Close price: %s" % dict['close price'], '\n')

