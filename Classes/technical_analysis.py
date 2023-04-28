import pandas as pd
import numpy as np

class TechnicalAnalysis:
    def __init__(self, stock_data):
        self.stock_data = stock_data

    def simple_moving_average(self, window):
        sma = self.stock_data['Close'].rolling(window=window).mean()
        return sma

    def relative_strength_index(self, window):
        delta = self.stock_data['Close'].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        avg_gain = gain.rolling(window=window).mean()
        avg_loss = loss.rolling(window=window).mean()

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

        return rsi

    def perform_analysis(self):
        # Perform technical analysis calculations
        # For example, calculate a 20-day simple moving average:
        sma_20 = self.simple_moving_average(20)
        print("20-day Simple Moving Average:\n", sma_20)

        # Return sample analysis data
        analysis_data = {'Sample Technical Analysis Data': 'This is a sample technical analysis result.'}
        return analysis_data