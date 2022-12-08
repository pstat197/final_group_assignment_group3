import pandas as pd 
import numpy as np 
import os

# Import the dataset containing info for 809 pokemons
pokemon = pd.read_csv(r'C:\Users\brian\OneDrive\Documents\Desktop\UCSB\Stats\Pstat197\final_group_assignment_group3\data\pokemon.csv')

# Sort the dataset by pokemon's name alphabetically and reassign the index
pokemon = pokemon.sort_values(by=['Name'], 
                              ascending=True).reset_index(drop=True)

path = "C:/Users/brian/OneDrive/Documents/Desktop/UCSB/Stats/Pstat197/final_group_assignment_group3/data/images/"

# Get all images' names in the image folder
nameOfImage = sorted(os.listdir(path))

# Initialize an empty list to store path to each image
pathOfImage = []
for i in nameOfImage:
    pathOfImage.append(path + i)

# Add a new column in the pokemon dataset with paths
pokemon['path'] = pathOfImage

# Initialize an empty list to store revised type of each pokemon
Type = []

count = pokemon.shape[0]

# We want only "Grass", "Fire", and "Water" and will classify all other types as "other"
for i in range(count):
    if (pokemon.iloc[i]['Type1']=='Grass') or (pokemon.iloc[i]['Type2']=='Grass'):
        Type.append('Grass')
    elif (pokemon.iloc[i]['Type1']=='Water') or (pokemon.iloc[i]['Type2']=='Water'):
        Type.append('Water')
    elif (pokemon.iloc[i]['Type1']=='Fire') or (pokemon.iloc[i]['Type2']=='Fire'):
        Type.append('Fire')
    else:
        Type.append('Other')

pokemon["type"]=Type
pokemon = pokemon.drop(['Type1', 'Type2'], axis=1)

pokemon.to_csv('pokemon_revised.csv')