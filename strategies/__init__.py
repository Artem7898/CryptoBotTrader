import pandas as pd
from strategies.mean_reversion import calculate_mean_reversion_signals

# Use the function as needed
data = pd.read_csv('data.csv')
signals = calculate_mean_reversion_signals(data)



