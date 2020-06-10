import pandas as pd

# The database

hockey_players = pd.read_csv('data/canucks.csv')

# Slice the rows and columns and save the new dataframe as `star_players`

star_players = hockey_players.loc[7:19, 'Player':'Country']

# Display it

star_players
