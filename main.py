#  INF601 - Advanced Programming in Python
#  Samuel Amoateng
#  Mini Project 1

# (5/5 points) Initial comments with your name, class and project at the top of your .py file.  -- Done
# (5/5 points) Proper import of packages used.  -- Done
# (20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your favorite stock tickers for the last 10 trading days. -- Done
# (10/10 points) Store this information in a list that you will convert to a array in NumPy. - Done
# (10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring the documentation for matplotlib. At minimum it just needs to show 10 data points. -- Done
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.


import yfinance as yf
import pprint
import numpy as np
import matplotlib.pyplot as plt
import  copy

mystocks = ['AAPL', 'MSFT', 'NVDA', 'GOOG', 'TSLA']
mystockdata = {}

for tickers in mystocks:
    dat=yf.Ticker(tickers)
    last10_days= (dat.history(period = '10d'))
    mystockdata[tickers] = []

    # I created a list of closing prices
    for prices in last10_days['Close']:
        mystockdata[tickers].append(prices)
    mystock = np.array(mystockdata[tickers])

    # I created a variable to determine High and Low prices within the last 10 days window
    high_low = copy.copy(mystockdata[tickers])
    high_low.sort()

    plt.plot(mystock)
    plt.title(tickers)
    plt.axis((0,10, high_low[0]-10,high_low[-1]+10))
    plt.ylabel("Closing Prices")
    plt.xlabel("Last 10 Trading days")

    # I saved the graphs into the chart directory
    plt.savefig(f'charts/{tickers}.png')
    plt.show()

