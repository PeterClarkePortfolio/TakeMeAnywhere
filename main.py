# Take me anywhere is a command based random location finder

import pandas as pd


def randomCity():
    # The below codes reads in a CSV excel document full of data about cities.
    citycsvread = pd.read_csv(r'worldcities.csv')
    listallcities = pd.DataFrame(citycsvread, columns=['city', 'country'])
    randomcitypandas = pd.DataFrame.sample(self=listallcities, n=1, frac=None, weights=None,
                                           random_state=None, axis=None)
    print(randomcitypandas)
    print("CSV City data provided by simplemaps.com/data/world-cities")
    # CSV City data provided by simplemaps.com/data/world-cities - free version


stop = False
while not stop:
    print("Please choose 1 for Random City or type 'close' to close the application")
    userInput = input(">>>")

    if userInput == "1":
        randomCity()
    elif userInput.lower() == "close":
        print("closing")
        stop = True
    else:
        print("Error, please type 1 or type close!")
