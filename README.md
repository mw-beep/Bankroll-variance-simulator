# Bankroll-variance-simulator
Simple Poker bankroll simulator, calculates possible outcomes given a winrate and standard deviation using Monte Carlo simulation.

Project outline:

1. Start with some defined bankroll value
2. Simulate monthly poker results using the given winrate and standard deviation, simulating monthly variance by drawing from a normal distribution
3. Repeat many times
4. Calculate summary statistics and print a report

Additional goals post MVP:
- plot outcomes on a graph using matplotlib, showing average, bottom 10% and top 10% bankroll outcomes. 