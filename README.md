# Bankroll-variance-simulator
Simple Poker bankroll simulator, calculates possible outcomes given a winrate and standard deviation using Monte Carlo simulation.

CURRENT FEATURES:

- Simulates one bankroll path over a chosen number of months
- Runs Monte Carlo simulations using configurable winrate, variance, hours, bankroll and simulation count
- Calculates summary statistics: average bankroll value at each point, median ending bankroll, 5th, 10th, 90th, 95th percentile outcomes, risk of ruin
- Prints a clear summary report
- Plots above summary statistics

Additional goals post MVP:
- plot outcomes on a graph using matplotlib, showing average, bottom 10% and top 10% bankroll outcomes. (COMPLETED)
- ask for user input as an alternative to using config file
- add probability of X months downswing
- add average downswing length
- add number of simulations in report and time taken to compute