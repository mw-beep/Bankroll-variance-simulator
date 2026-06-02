import numpy as np

def calculate_summary(all_paths):

    ending_bankrolls = all_paths[:,-1]
    average_bankroll = np.mean(ending_bankrolls)

    bottom_10_percentile = np.percentile(ending_bankrolls,10)
    top_10_percentile = np.percentile(ending_bankrolls,90)

    bottom_5_percentile = np.percentile(ending_bankrolls, 5)
    top_5_percentile = np.percentile(ending_bankrolls, 95)

    hit_zero = np.any(all_paths<=0, axis = 1)
    risk_of_ruin = np.mean(hit_zero)    

    results = {'average_ending_bankroll': average_bankroll,
               'top_10_percentile': top_10_percentile,
               'top_5_percentile': top_5_percentile,
               'bottom_10_percentile': bottom_10_percentile,
               'bottom_5_percentile': bottom_5_percentile,
               'risk_of_ruin': risk_of_ruin}
    
    return results
    