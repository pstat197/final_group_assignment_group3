import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import os
import seaborn as sns


# Import the dataset containing info for 809 pokemons
pokemon = pd.read_csv(r'C:\Users\brian\OneDrive\Documents\Desktop\UCSB\Stats\Pstat197\final_group_assignment_group3\data\pokemon.csv')

# Sort the dataset by pokemon's name alphabetically and reassign the index
pokemon = pokemon.sort_values(by=['Name'], 
                              ascending=True).reset_index(drop=True)

# Check the basic info of the dataset
display(pokemon.head())
display(pokemon.describe())
display(pokemon['Type1'].unique())

# Make a list of all pokemon types based on Type1 and Type2 columns
X=pokemon['Type1'].tolist()+pokemon["Type2"].tolist()

# Plot the types and their corresponding counts
plt.figure(figsize=(14, 6))
sns.histplot(x=X)
plt.title('Types of pokemon')
plt.show()

import matplotlib.image as mpimg

# Specify the path to image folder on the local computer. Modify it to user's discretion
path = "C:/Users/brian/OneDrive/Documents/Desktop/UCSB/Stats/Pstat197/final_group_assignment_group3/data/images/"

# Specify the number of plots and how we want it to be displayed
fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(1, 5, figsize=(15, 8)) 
ax = [ax1, ax2, ax3, ax4, ax5]

# This for loop retrieves the path to the first 5 images and plot
for i in range(5):
    img = mpimg.imread(path+pokemon['Name'][i]+'.png')
    ax[i].imshow(img)
    ax[i].set_title(pokemon['Name'][i])
    ax[i].axis('off')
plt.tight_layout()
plt.show()

