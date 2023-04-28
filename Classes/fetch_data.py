import yfinance as yf
import pandas as pd

class FetchData:
    def __init__(self, symbols, start_date, end_date):
        self.symbols = symbols
        self.start_date = start_date
        self.end_date = end_date
        self.stock_data = pd.DataFrame()
        self.stock_list_error = []
        self.stock_list_good = []

    def fetch_stock_data(self):
        # Fetch S&P 500, Nasdaq, and Russell 2000 data
        indices = ['^GSPC', '^IXIC', '^RUT']
        for index in indices:
            try:
                data = yf.download(index, start=self.start_date, end=self.end_date)
                if not data.empty:
                    data = data.reset_index()
                    data.sort_values(by=['Date'], inplace=True, ascending=False)
                    data.insert(0, "Symbol", index)
                    self.stock_data = pd.concat([self.stock_data, data], axis=0)
                    print("Good Stock: " + index)
                    self.stock_list_good.append(index)
                else:
                    print("Error Stock: " + index)
                    self.stock_list_error.append(index)
            except Exception as e:
                print(f"Error fetching data for {index}: {e}")
                self.stock_list_error.append(index)

        # Fetch data for selected stocks
        for symbol in self.symbols:
            try:
                temp = yf.download(symbol, start=self.start_date, end=self.end_date)
                if not temp.empty:
                    temp = temp.reset_index()
                    temp.sort_values(by=['Date'], inplace=True, ascending=False)
                    temp.insert(0, "Symbol", symbol)
                    self.stock_data = pd.concat([self.stock_data, temp], axis=0)
                    print("Good Stock: " + symbol)
                    self.stock_list_good.append(symbol)
                else:
                    print("Error Stock: " + symbol)
                    self.stock_list_error.append(symbol)
            except Exception as e:
                print(f"Error fetching data for {symbol}: {e}")
                self.stock_list_error.append(symbol)

    def get_stock_data(self):
        return self.stock_data

    def get_good_stocks(self):
        return self.stock_list_good

    def get_error_stocks(self):
        return self.stock_list_error