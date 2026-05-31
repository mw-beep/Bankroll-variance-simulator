import numpy as np

def simulate_one_path(starting_bankroll, hourly_winrate, hourly_std_dev, hours_per_month, months):

    bankroll = starting_bankroll
    history = [bankroll]
    monthly_mean = hourly_winrate*hours_per_month
    monthly_std = hourly_std_dev*np.sqrt(hours_per_month)

    for month in range(months):
        profit = np.random.normal(monthly_mean,monthly_std)
        bankroll += profit
        history.append(bankroll)
    
    return history
