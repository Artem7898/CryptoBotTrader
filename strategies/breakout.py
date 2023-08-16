# Assuming you have fetched historical data into a pandas DataFrame called 'historical_data'

def buy_on_rise_strategy(data):
    positions = []
    for i in range(1, len(data)):
        if data['Price'][i] > data['Price'][i - 1]:
            positions.append(('buy', data['Timestamp'][i], data['Price'][i]))

    return positions

positions = buy_on_rise_strategy(historical_data)
print("Positions:", positions)
