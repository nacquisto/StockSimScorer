class DataDisplay:
    def __init__(self, stock_data, analysis_data):
        self.stock_data = stock_data
        self.analysis_data = analysis_data

    def display_data(self):
        print("Displaying Stock Data:")
        print(self.stock_data)
        print("\nDisplaying Analysis Data:")
        print(self.analysis_data)