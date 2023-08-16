import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from flask import Flask, render_template
import ccxt
import os


app = Flask(__name__)

# Read data from CSV file
data = pd.read_csv('data.csv')


@app.route('/')
def index():
    return render_template('index.html', data=data)


def fetch_ticker_and_save():
    try:
        exchange = ccxt.binance()  # Replace with your preferred exchange
        ticker = exchange.fetch_ticker('BTC/USDT')

        ticker_path = os.path.join('ticker_results', 'ticker.txt')
        with open(ticker_path, 'w') as f:
            f.write(format_ticker_data(ticker))
        print("Ticker data saved successfully.")
    except Exception as e:
        print("Error fetching or saving ticker data:", e)


def format_ticker_data(ticker_data):
    formatted_data = []
    for key, value in ticker_data.items():
        formatted_data.append(f"{key}: {value}")
    return '\n'.join(formatted_data)


if __name__ == '__main__':
    fetch_ticker_and_save()  # Fetch ticker data and save to file
    app.run(debug=True)


class CryptoBotTraderGUI(QMainWindow):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("CryptoBotTrader")
        self.setGeometry(100, 100, 800, 600)

        table = QTableWidget(self)
        table.setGeometry(50, 50, 700, 500)
        table.setColumnCount(len(self.data.columns))
        table.setHorizontalHeaderLabels(self.data.columns)

        for row_index, row_data in self.data.iterrows():
            table.insertRow(row_index)
            for col_index, value in enumerate(row_data):
                table.setItem(row_index, col_index, QTableWidgetItem(str(value)))

        self.show()


def main():
    data = pd.read_csv('data.csv')  # Load CSV data
    app = QApplication(sys.argv)
    window = CryptoBotTraderGUI(data)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
