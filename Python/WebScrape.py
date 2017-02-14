import pandas_datareader as pdr
from datetime import datetime
import os
import urllib
import json
import pandas as pd
import re
import pyperclip
import io

output_folder = 'D:\\UIUC\\CS411\\Project\\'

htmlfile = urllib.urlopen("http://data.okfn.org/data/core/s-and-p-500-companies/r/constituents.csv")
tickers = pd.read_csv(htmlfile)

df = pd.DataFrame()
count = 0
for ticker in tickers.loc[:,'Symbol']:
    url = "http://chart.finance.yahoo.com/table.csv?s=" + ticker + "&a=0&b=1&c=2001&d=11&e=31&f=2016&g=d&ignore=.csv"
    tmp = pd.read_csv(url)
    tmp['ticker'] = ticker
    df = df.append(tmp)
    count += 1
    print count, ticker
df.to_csv(output_folder + 'PriceHistory.csv')

#df = pd.DataFrame()
#count = 0
#for ticker in tickers.loc[38:len(tickers),'Symbol']:
#    tmp = pdr.get_data_yahoo(symbols=ticker, start=datetime(2000, 1, 1), end=datetime(2017, 1, 1))
#    tmp['ticker'] = ticker
#    df = df.append(tmp)
#    count += 1
#    print count, ticker
#df.to_csv(output_folder + 'PriceHistory.csv')

columns = ['ticker', 'prev_close', 'open', 'day_range', 'year_range', 'volume', 'avg_volume', 
                                   'market_cap', 'beta', 'PE', 'EPS', 'div_yield', 'ex_div_date', 'target']
df_summary = pd.DataFrame(columns=columns)
ticker = 'ABT'
count = 0
for ticker in tickers.loc[451:len(tickers),'Symbol']:
    #summary, statistics, profiles, financials
    url_summary = "https://finance.yahoo.com/quote/" + ticker
    url_stats = "https://finance.yahoo.com/quote/" + ticker + "/key-statistics"
    url_profile = "https://finance.yahoo.com/quote/" + ticker + "/profile"
    url_fin = "https://finance.yahoo.com/quote/" + ticker + "/financials"
    htmlfile = urllib.urlopen(url_summary)
    htmltext = htmlfile.read()
    regex = 'data-test=\"PREV_CLOSE-value\" data-reactid=\"[0-9]+\">(.+?)</td>'
    #pattern = re.compile(regex)
    previous_close = re.findall(regex, htmltext)[0]
    
    regex = 'data-test=\"OPEN-value\" data-reactid=\"[0-9]+\">(.+?)</td>' 
    open_price = re.findall(regex, htmltext)[0] 
    
    regex = 'data-test=\"DAYS_RANGE-value\" data-reactid=\"[0-9]+\">(.+?)</td>'
    day_range = re.findall(regex, htmltext)[0]
    
    regex = 'data-test=\"FIFTY_TWO_WK_RANGE-value\" data-reactid=\"[0-9]+\">(.+?)</td>'
    year_range = re.findall(regex, htmltext)[0]
    
    regex = 'data-test=\"TD_VOLUME-value\" data-reactid=\"[0-9]+\">(.+?)</td>'
    volume = re.findall(regex, htmltext)[0]
    
    regex = 'data-test=\"AVERAGE_VOLUME_3MONTH-value\" data-reactid=\"[0-9]+\">(.+?)</td>'
    avg_volume = re.findall(regex, htmltext)[0]
    
    regex = 'data-test=\"MARKET_CAP-value\" data-reactid=\"[0-9]+\">(.+?)</td>'
    market_cap = re.findall(regex, htmltext)[0]
    
    regex = 'data-test=\"BETA-value\" data-reactid=\"[0-9]+\">(.+?)</td>'
    beta = re.findall(regex, htmltext)[0]
    
    regex = 'data-test=\"PE_RATIO-value\" data-reactid=\"[0-9]+\">(.+?)</td>'
    PE = re.findall(regex, htmltext)[0]
    
    regex = 'data-test=\"EPS_RATIO-value\" data-reactid=\"[0-9]+\">(.+?)</td>'
    EPS = re.findall(regex, htmltext)[0]
    
    #regex = 'data-test=\"EARNINGS_DATE-value\" data-reactid=\"417\"><span>(.+?)</span>'
    #earning_date = re.findall(regex, htmltext)
    
    regex = 'data-test=\"DIVIDEND_AND_YIELD-value\" data-reactid=\"[0-9]+\">(.+?)</td>'
    div_yield = re.findall(regex, htmltext)[0]
    
    regex = 'data-test=\"EXDIVIDEND_DATE-value\" data-reactid=\"[0-9]+\">(.+?)</td>'
    ex_div_date = re.findall(regex, htmltext)[0]
    
    regex = 'data-test=\"ONE_YEAR_TARGET_PRICE-value\" data-reactid=\"[0-9]+\">(.+?)</td>'
    target = re.findall(regex, htmltext)[0]
    df_summary.ix[ticker] = [ticker, previous_close, open_price, day_range, year_range, volume, avg_volume, 
        market_cap, beta, PE, EPS, div_yield, ex_div_date, target]
    count +=1
    print count
df_summary.to_csv(output_folder + "CompanySummary.csv")

keywords = ['enterpriseValue', 'forwardPE', 'profitMargins', 'floatShares', 'sharesOutstanding', 'sharesShort', 'sharesShortPriorMonth', 
            'heldPercentInsiders', 'heldPercentInstitutions', 'shortRatio', 'shortPercentOfFloat', 'beta', 'bookValue', 'priceToBook', 
            'earningsQuarterlyGrowth', 'netIncomeToCommon', 'trailingEps', 'forwardEps', 'pegRatio', 'enterpriseToRevenue', 'enterpriseToEbitda', 
            'address1', 'city', 'state', 'zip', 'country', 'website', 'industry', 'sector', 'longBusinessSummary', 'fullTimeEmployees', 
            'totalCash', 'totalCashPerShare', 'ebitda', 'totalDebt', 'totalRevenue', 'debtToEquity', 'revenuePerShare', 'returnOnEquity', 
            'grossProfits', 'earningsGrowth', 'revenueGrowth', 'grossMargins', 'ebitdaMargins', 'operatingMargins', 'profitMargins']
df = pd.DataFrame(columns=keywords)
ticker = 'ABT'
count = 0
for ticker in tickers.loc[:len(tickers),'Symbol']:
    ls = []
    #summary, statistics, profiles, financials
    url = 'https://query1.finance.yahoo.com/v11/finance/quoteSummary/'+ticker+'?lang=en-US&region=US&corsDomain=finance.yahoo.com&crumb=Tl3yH%2Fwsfsg&modules=calendarEvents%2CdefaultKeyStatistics%2Cearnings%2CfinancialData%2CrecommendationTrend%2CsummaryProfile%2CupgradeDowngradeHistory&shouldFormat=false'
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    for key in keywords:
        regex = '\"'+key+'\":(.+?),\"' 
        try:
            record = re.findall(regex, htmltext)[0] 
            ls.append(record)
        except IndexError:
            ls.append(None)
    df.ix[ticker] = ls
    count +=1
    print count, ticker
df.to_csv(output_folder + "CompanyProfile.csv")

url = 'https://finance.yahoo.com/quote/' + ticker + '/analysts'
url_not_tried_yet = 'https://l1-query.finance.yahoo.com/v7/finance/chart/ABT?range=1d&interval=1m&indicators=quote&includeTimestamps=true&includePrePost=false&corsDomain=finance.yahoo.com'
#Tickers that cannot be found: HOT, TYC

