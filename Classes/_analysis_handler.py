# from technical_analysis import TechnicalAnalysis
# from fundamental_analysis import FundamentalAnalysis

# class AnalysisHandler:
#     def __init__(self, stock_data, good_stocks, analysis_type):
#         self.stock_data = stock_data
#         self.good_stocks = good_stocks
#         self.analysis_type = analysis_type

#     def perform_analysis(self):
#         if self.analysis_type == "technical":
#             technical_analysis = TechnicalAnalysis(self.stock_data)
#             # Perform technical analysis calculations
#             # For example, calculate a 20-day simple moving average:
#             sma_20 = technical_analysis.simple_moving_average(20)
#             print("20-day Simple Moving Average:\n", sma_20)
#             return analysis_data

#         elif self.analysis_type == "fundamental":
#             fundamental_analysis = FundamentalAnalysis(self.good_stocks)
#             financial_info = fundamental_analysis.get_financial_info()
#             print("Financial Info:\n", financial_info)
#             return analysis_data