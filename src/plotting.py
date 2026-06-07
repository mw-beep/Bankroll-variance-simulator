import matplotlib.pyplot as plt
import numpy as np

def plot(all_paths, num_simulations):

    sorted_results = all_paths[np.argsort(all_paths[:,-1])]

    bottom_5_path = sorted_results[int(num_simulations * 0.05)]
    top_5_path = sorted_results[int(num_simulations * 0.95)]

    bottom_10_path = sorted_results[int(num_simulations * 0.1)]
    top_10_path = sorted_results[int(num_simulations * 0.9)]

    average_path = sorted_results[int(num_simulations * 0.5)]

    x_axis = np.arange(all_paths.shape[1])
    plt.plot(x_axis, bottom_5_path, marker='x', label = 'Bottom 5% path')
    plt.plot(x_axis, bottom_10_path, marker='x', label = 'Bottom 10% path')
    plt.plot(x_axis, average_path, marker='x', label = 'Average path')
    plt.plot(x_axis, top_5_path, marker='x', label = 'Top 5% path')
    plt.plot(x_axis, top_10_path, marker='x', label = 'Top 10% path')

    plt.axhline(0, linestyle ='--', linewidth = 1, color = 'black')
    plt.xticks(x_axis)
    plt.grid(True, alpha = 0.3)

    plt.xlabel('Month')
    plt.ylabel('Bankroll')
    plt.title('Selected bankroll simulation paths')
    plt.legend()
    plt.show()