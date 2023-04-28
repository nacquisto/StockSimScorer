from Classes.file_handler import StockDataFileSelection
from Classes.stock_selection import SectorStockSelection
from Classes.fetch_data import FetchData
from Classes.chart_data import ChartData
from Classes.analysis_type_selection import AnalysisTypeSelection
from Classes.technical_analysis import TechnicalAnalysis
from Classes.fundamental_analysis import FundamentalAnalysis
from Classes.data_display import DataDisplay
from Classes.output_path import Output

class UserInputHandler:
    def __init__(self, csv_folder):
        self.csv_folder = csv_folder

    def get_user_input(self):
        # Select stock data file
        file_selector = StockDataFileSelection(self.csv_folder)

        file_selector.show_options()
        user_choice = int(input("Enter the number corresponding to the stock data file you want to use: "))

        selected_stock_data = file_selector.select_stock_data_file(user_choice)

        # Select stock symbols
        stock_selector = SectorStockSelection(selected_stock_data)
        
        # Choose the sectors
        chosen_sectors = stock_selector.select_sectors()

        # Filter and select symbols from the chosen sectors
        selected_symbols = stock_selector.select_symbols(chosen_sectors)
        print("Selected stock symbols:", selected_symbols)

        # Set date range
        stock_selector.set_date_range()

        # Fetch stock data
        fetcher = FetchData(selected_symbols, stock_selector.start_date, stock_selector.end_date)
        fetcher.fetch_stock_data()

        stock_data, good_stocks, error_stocks = fetcher.get_stock_data(), fetcher.get_good_stocks(), fetcher.get_error_stocks()
        
        # # Save stock data to CSV
        # stock_data_output = Output(stock_data, None)
        # stock_data_output.save_stock_data_to_csv("CSV/stock_data.csv")

        # Plot stock data
        chart_data = ChartData(stock_data)
        chart_data.plot_stock_data()

        # Select analysis type
        analysis_type_selector = AnalysisTypeSelection()
        analysis_type_selector.show_options()
        selected_analysis_type = analysis_type_selector.select_analysis_type()
        print("Selected analysis type:", selected_analysis_type)

        # Perform analysis
        if selected_analysis_type == "technical":
            analysis = TechnicalAnalysis(stock_data)
            analysis_data = analysis.perform_analysis()
        elif selected_analysis_type == "fundamental":
            analysis = FundamentalAnalysis(stock_data)
            analysis_data = analysis.perform_analysis()

        # Display data
        data_display = DataDisplay(stock_data, analysis_data)
        data_display.display_data()

        # Save data to CSV
        output = Output(stock_data, analysis_data)
        output.save_stock_data_to_csv("CSV/stock_data.csv")
        output.save_analysis_data_to_csv("CSV/analysis_data.csv")

        return stock_data, good_stocks, error_stocks


    # def system_output(self, stock_data, good_stocks, error_stocks, analysis_data):
    #     # Save stock data to CSV
    #     stock_data_output = Output(stock_data)
    #     stock_data_output.save_stock_data_to_csv("CSV/stock_data.csv")

    #     #Save analysis data to CSV
    #     analysis_data_output = Output(analysis_data)
    #     analysis_data_output.save_analysis_data_to_csv("CSV/analysis_data.csv")   

    #     # # Display data
    #     data_display = DataDisplay(stock_data, analysis_data)
    #     data_display.display_data()