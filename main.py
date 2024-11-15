# Header

# Libraries
from Functions.math_utilities import calculate_circumference as cc


# Functions


if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
    a = cc(5)
    #a = mu.calculate_circumference(5)
    print(a)
else:
    print(f"This module is called {__name__} and is being called by another script")




