from src import config
from src.simulator import simulate_one_path, simulate_many_paths

path = simulate_one_path(starting_bankroll=config.STARTING_BANKROLL, 
                         hourly_winrate=config.HOURLY_WINRATE, 
                         hourly_std_dev=config.HOURLY_STD_DEV, 
                         hours_per_month=config.HOURS_PER_MONTH, 
                         months=config.MONTHS)
print(path)
print(len(path))

sim_number = 10_000

all_paths = simulate_many_paths(starting_bankroll=config.STARTING_BANKROLL, 
                         hourly_winrate=config.HOURLY_WINRATE, 
                         hourly_std_dev=config.HOURLY_STD_DEV, 
                         hours_per_month=config.HOURS_PER_MONTH, 
                         months=config.MONTHS, num_sims=sim_number)

print("------------MANY PATHS-----------")
print(all_paths)
print(all_paths.shape)