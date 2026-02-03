import yfinance as yf
import pandas as pd
import os
from datetime import datetime

def downloadData():
    
    tickerSymbol = "SPY"
    startDate = "2020-01-01"
    endDate = datetime.today().strftime('%Y-%m-%d')
    
    print(f"Downloading data for {tickerSymbol} from {startDate} to {endDate}...")
    data = yf.download(tickerSymbol, start=startDate, end=endDate)
    
    outputDir = "data/raw"
    os.makedirs(outputDir, exist_ok=True)
    
    outputFile = os.path.join(outputDir, "spy_data.csv")
    data.to_csv(outputFile)
    
    print(f"Success! Data saved to {outputFile}")

if __name__ == "__main__":
    downloadData()
