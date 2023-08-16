import pandas as pd


def calculate_mean_reversion_signals(data, lookback_window=10, z_threshold=1.0):
    signals = []

    for i in range(lookback_window, len(data)):
        window = data['Price'][i - lookback_window:i]
        window_mean = window.mean()
        window_std = window.std()
        current_price = data['Price'][i]

        z_score = (current_price - window_mean) / window_std

        if z_score > z_threshold:
            signals.append(('SELL', data['Timestamp'][i], current_price))
        elif z_score < -z_threshold:
            signals.append(('BUY', data['Timestamp'][i], current_price))

    return signals


# This code will be executed if mean_reversion.py is run directly
if __name__ == "__main__":
    data = pd.read_csv('data.csv')  # Load data for testing
    signals = calculate_mean_reversion_signals(data)

    for signal in signals:
        print(f"{signal[0]} signal at {signal[1]} - Price: {signal[2]}")


"""
In this example, the calculate_mean_reversion_signals function calculates 
mean reversion signals based on a specified lookback window and z-score threshold.
It considers buying when the price is below a certain negative threshold and selling 
when the price is above a positive threshold.
You can modify and expand this example to suit your needs, including integrating 
it with your main application logic, setting appropriate parameters,
 and considering risk management strategies.
Remember that trading strategies should be thoroughly tested using historical data
and validated before being used in a real trading environment.
"""