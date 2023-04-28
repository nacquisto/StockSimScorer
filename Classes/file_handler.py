import pandas as pd
import os

class StockDataFileSelection:
    def __init__(self, csv_folder):
        self.csv_folder = csv_folder
        self.available_files = {
            1: 'SP500.csv',
            2: 'DOW30.csv',
            3: 'RUSSELL2000.csv'
        }

    def show_options(self):
        print("Available stock data files:")
        for key, value in self.available_files.items():
            print(f"{key}: {value}")

    def _is_valid_option(self, option):
        if isinstance(option, int) and option in self.available_files:
            return True
        else:
            print("Invalid option. Please choose from the available options.")
            return False

    def select_stock_data_file(self, option):
        if self._is_valid_option(option):
            file_path = os.path.join(self.csv_folder, self.available_files[option])
            try:
                stock_data = pd.read_csv(file_path)
                return stock_data
            except FileNotFoundError:
                print(f"File not found: {file_path}")
                return None
            except Exception as e:
                print(f"An error occurred while reading the file: {file_path}")
                print(f"Error: {e}")
                return None
        else:
            return None