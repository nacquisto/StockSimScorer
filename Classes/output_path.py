import pandas as pd

class Output:
    def __init__(self, stock_data, analysis_data=None):
        self.stock_data = stock_data
        self.analysis_data = analysis_data

    def save_stock_data_to_csv(self, stock_data_filename='CSV/stock_data.csv'):
        self.stock_data.to_csv(stock_data_filename, index=False)

    def save_analysis_data_to_csv(self, analysis_data_filename='CSV/analysis_data.csv'):
        if self.analysis_data is not None:
            self.analysis_data.to_csv(analysis_data_filename, index=False)