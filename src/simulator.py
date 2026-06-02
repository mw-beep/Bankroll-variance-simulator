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

def simulate_many_paths(starting_bankroll, hourly_winrate, hourly_std_dev, hours_per_month, months, num_sims):

    all_paths = np.zeros((num_sims, months+1))

    for sim in range(num_sims):
        path = simulate_one_path(starting_bankroll, hourly_winrate, hourly_std_dev, hours_per_month, months)
        all_paths[sim] = path
    
    return all_paths

