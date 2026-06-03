from src.config import MONTHS

def summary_report(results):

    print('BANKROLL SIMULATION RESULTS\n ------------------------- \n\n' f'\n Months: {MONTHS}'
          f'\nAverage ending bankroll: £{results["average_ending_bankroll"]:,.2f}'
          f'\n 10th percentile outcome: £{results["bottom_10_percentile"]:,.2f} '
          f'\n 5th percentile outcome: £{results["bottom_5_percentile"]:,.2f} '
          f'\n 90th percentile outcome: £{results["top_10_percentile"]:,.2f} '
          f'\n 95th percentile outcome: £{results["top_5_percentile"]:,.2f} ') 