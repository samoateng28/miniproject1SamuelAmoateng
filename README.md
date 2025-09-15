### INF601 - Advanced Programming in Python
### Samuel Amoateng
### Mini Project 1
 
 
# Project Title
Stock Price Visualization with NumPy and Matplotlib.
 
## Description
 
This project focusses on getting and visualising stock market data in Python.  Using the yfinance API, the software gets the most recent closing prices for five selected stock tickers over the last ten days.  The data is kept in lists, turned into NumPy arrays for easy processing, and then projected onto individual graphs using Matplotlib.  Each graph provides a clear visual representation of stock performance, making it easier to identify short-term patterns and variations.  The application saves the graphs as PNG files in a charts folder, making the results replicable and easily accessible.
 
## Getting Started
 
### Dependencies
kindly install this pip requirements:
```
pip install -r requirements.txt
```

### Executing program
 ```
python main.py
```
 
## Authors
Samuel Amoateng

## Version History
* 0.1
    * Initial Release
## Acknowledgments
Inspiration, code snippets, etc.
* [matplotlib documentation](https://matplotlib.org/stable/index.html)
* [yfinance documentation](https://ranaroussi.github.io/yfinance/index.html)
