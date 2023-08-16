import logging


class Metrics:
    def __init__(self):
        self.trades_executed = 0
        self.successful_trades = 0
        self.failed_trades = 0

    def log_trade(self, success=True):
        self.trades_executed += 1
        if success:
            self.successful_trades += 1
        else:
            self.failed_trades += 1
        logging.info("Trade Executed: Success=%s", success)

    def print_metrics(self):
        logging.info("Total Trades Executed: %s", self.trades_executed)
        logging.info("Successful Trades: %s", self.successful_trades)
        logging.info("Failed Trades: %s", self.failed_trades)


"""
In this example, the Metrics class provides basic functionality
to track and log trade execution metrics. The class keeps count of total trades executed,
successful trades, and failed trades. The log_trade method updates the metrics based
on whether the trade was successful or not. The print_metrics method logs the metrics for review.
Remember that this is a simplified example, 
and you can expand this class to include more detailed metrics, 
performance indicators, and tracking relevant to your trading strategy. 
Proper logging helps you understand the behavior of your bot and analyze its performance over time.
You can incorporate this Metrics class into your trading strategy
logic and call its methods whenever you execute trades or perform other relevant actions.
"""