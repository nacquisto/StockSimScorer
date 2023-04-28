import matplotlib.pyplot as plt
import seaborn as sns

class ChartData:
    def __init__(self, stock_data):
        self.stock_data = stock_data

    def plot_stock_data(self):
        sns.set(style="darkgrid")

        for symbol in self.stock_data['Symbol'].unique():
            stock = self.stock_data[self.stock_data['Symbol'] == symbol]
            plt.plot(stock['Date'], stock['Close'], label=symbol)

        plt.xlabel("Date")
        plt.ylabel("Closing Price")
        plt.title("Stock Data")
        plt.legend()
        plt.show()