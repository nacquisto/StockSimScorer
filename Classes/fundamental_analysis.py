import yfinance as yf

class FundamentalAnalysis:
    def __init__(self, stock_symbols):
        self.stock_symbols = stock_symbols

    def get_financial_info(self):
        financial_data = {}
        for symbol in self.stock_symbols:
            stock = yf.Ticker(symbol)
            financial_data[symbol] = stock.info

        return financial_data

    def perform_analysis(self):
        financial_info = self.get_financial_info()

        analysis_data = {}
        for symbol, info in financial_info.items():
            analysis_data[symbol] = {}
            
            # Calculate P/E ratio
            pe_ratio = info.get('trailingPE', None)
            analysis_data[symbol]['P/E Ratio'] = pe_ratio

            # Calculate P/B ratio
            pb_ratio = info.get('priceToBook', None)
            analysis_data[symbol]['P/B Ratio'] = pb_ratio

            # Calculate dividend yield
            dividend_yield = info.get('dividendYield', None)
            analysis_data[symbol]['Dividend Yield'] = dividend_yield

            # Calculate debt-to-equity ratio
            debt_to_equity = info.get('debtToEquity', None)
            analysis_data[symbol]['Debt-to-Equity Ratio'] = debt_to_equity

        return analysis_data