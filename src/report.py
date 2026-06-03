

def summary_report(results, months, starting_bankroll):

    print('BANKROLL SIMULATION RESULTS\n ------------------------- ' f'\n Months: {months} \n'
          f'\nStarting bankroll: £{starting_bankroll}'
          f'\nAverage ending bankroll: £{results["average_ending_bankroll"]:,.2f}\n'
          f'\n 10th percentile outcome: £{results["bottom_10_percentile"]:,.2f} '
          f'\n 5th percentile outcome: £{results["bottom_5_percentile"]:,.2f} '
          f'\n 90th percentile outcome: £{results["top_10_percentile"]:,.2f} '
          f'\n 95th percentile outcome: £{results["top_5_percentile"]:,.2f} ') 