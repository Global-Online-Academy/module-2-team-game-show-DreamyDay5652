# YOU ONLY HAVE TO SUBMIT FUNCTIONS FOR WHICH
# YOU ARE THE DRIVER IN PAIR PROGRAMMING

import random

# Here are some history variables to test your code on. Feel free to create your own.
hist1 = []
hist2 = [("split","steal")]
hist3 = [("split","split"),("steal","split"),("split,steal"),("split,split"),("steal,split")]
hist4 = [("split","steal"),("steal","steal"),("split","steal"),("steal","split"),("split","split"),("steal","split")]

# Your team's 1st strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 


# Your team's 2nd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 


# Your team's 3rd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
def codeCrafters3(history):
    opp_hist = [move[1] for move in history]

    if len(opp_hist) < 3:
        return 'steal'
    
    splits = opp_hist.count('split')
    steals = opp_hist.count('steal')
    total = len(opp_hist)

    if splits / total > 0.5:
        return 'steal'
    
    if steals / total > 0.5:
        if random.random() < 0.7:
            return 'steal'
        else:
            return 'split'
    
    if random.random() < 0.6:
        return 'steal'
    else:
        return'split'

