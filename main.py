from src import config
from src.simulator import simulate_one_path, simulate_many_paths
from src.stats import calculate_summary
from src.report import summary_report
from src.plotting import plot

path = simulate_one_path(starting_bankroll=config.STARTING_BANKROLL, 
                         hourly_winrate=config.HOURLY_WINRATE, 
                         hourly_std_dev=config.HOURLY_STD_DEV, 
                         hours_per_month=config.HOURS_PER_MONTH, 
                         months=config.MONTHS)


all_paths = simulate_many_paths(starting_bankroll=config.STARTING_BANKROLL, 
                         hourly_winrate=config.HOURLY_WINRATE, 
                         hourly_std_dev=config.HOURLY_STD_DEV, 
                         hours_per_month=config.HOURS_PER_MONTH, 
                         months=config.MONTHS, num_sims=config.NUM_SIMULATIONS)



results = calculate_summary(all_paths)


print('-------------------------')

summary_report(results, months=config.MONTHS, starting_bankroll=config.STARTING_BANKROLL)
plot(all_paths, num_simulations=config.NUM_SIMULATIONS)
