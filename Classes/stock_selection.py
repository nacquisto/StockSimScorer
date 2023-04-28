import pandas as pd
from datetime import datetime

class SectorStockSelection:
    def __init__(self, stock_data):
        self.stock_data = stock_data
        self.unique_sectors = self.stock_data['Sector'].unique()

    def select_sectors(self):
        print("Available sectors:")
        for idx, sector in enumerate(self.unique_sectors):
            print(f"{idx}: {sector}")

        chosen_sectors = []
        while True:
            user_choice = input("Enter the number corresponding to the sector you want to analyze or 'done' to finish: ")
            if user_choice.lower() == 'done':
                break
            try:
                chosen_sectors.append(self.unique_sectors[int(user_choice)])
                print(f"Selected sector(s): {', '.join(chosen_sectors)}")
            except IndexError:
                print("Invalid option. Please choose from the available options.")
            except ValueError:
                print("Invalid input. Please enter a valid number or 'done'.")

        return chosen_sectors

    def select_symbols(self, chosen_sectors):
        sector_stocks = self.stock_data[self.stock_data['Sector'].isin(chosen_sectors)]
        print("Available stocks in the selected sector(s):")
        for idx, symbol in enumerate(sector_stocks['Symbol']):
            print(f"{idx}: {symbol}")

        selected_symbols = []
        while True:
            user_choice = input("Enter the number corresponding to the stock symbol you want to analyze or 'done' to finish: ")
            if user_choice.lower() == 'done':
                break
            try:
                selected_symbols.append(sector_stocks.iloc[int(user_choice)]['Symbol'])
                if len(selected_symbols) >= 2:
                    print("You have reached the maximum of 2 stocks.")
                    break
            except IndexError:
                print("Invalid option. Please choose from the available options.")
            except ValueError:
                print("Invalid input. Please enter a valid number or 'done'.")

        return selected_symbols

    def _validate_date(self, date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def set_date_range(self):
        while True:
            self.start_date = input("Enter the start date for stock data in YYYY-MM-DD format: ")
            if self._validate_date(self.start_date):
                break
            else:
                print("Invalid date format. Please use YYYY-MM-DD format.")

        while True:
            self.end_date = input("Enter the end date for stock data in YYYY-MM-DD format: ")
            if self._validate_date(self.end_date):
                break
            else:
                print("Invalid date format. Please use YYYY-MM-DD format.")