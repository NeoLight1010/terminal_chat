"""Special functions to control/style the terminal in which the program is running."""

from blessings import Terminal

t = Terminal() # initialize blessings for colors

def high_prior(txt): # High priority texts as [STARTING] will be printed red.
    return t.red(txt)

def medium_prior(txt): # Medium priority texts as [STARTING] will be printed red.
    return t.yellow(txt)

def low_prior(txt): # Medium priority texts as [STARTING] will be printed red.
    return t.green(txt)