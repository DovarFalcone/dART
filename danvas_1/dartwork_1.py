import matplotlib.pyplot as plt
import pandas as pd
import random

# Load the public data set (example: Iris dataset)
data = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')

# Extract the features/columns from the data
features = data.columns[:-1].tolist()

# Generate abstract art using random combinations of the features
fig, ax = plt.subplots(figsize=(8, 6), facecolor='black')  # Set background color

for _ in range(100):
    # Randomly select two features
    x_feature, y_feature = random.sample(features, 2)

    # Generate random indices to select data points
    indices = data.sample(30).index

    # Get the values of the selected features
    x = data.loc[indices, x_feature]
    y = data.loc[indices, y_feature]

    # Generate random color and marker style
    color = (random.random(), random.random(), 0.6)  # Random RGB color
    marker = random.choice([
                            '.',   # Point marker
                            ',',   # Pixel marker
                            'o',   # Circle marker
                            'v',   # Downward pointing triangle marker
                            '^',   # Upward pointing triangle marker
                            '2',   # Upward pointing triangle marker
                            's',   # Square marker
                            'p',   # Pentagon marker
                            '*',   # Star marker
                            'h',   # Hexagon1 marker
                            'H',   # Hexagon2 marker
                            'D'    # Diamond marker
                            ])  # Random marker shape
    linestyle = random.choice(['solid', 'dashdot', 'dotted']) # Random linestyle

    random_nums = [3,4,5,6,7,8,9,10]
    rand_idx = int(random.random() * len(random_nums))
    random_num = random_nums[rand_idx]  

    # Plot the data points with lines
    ax.plot(x, y, 
            marker=marker, 
            markersize=random_num, 
            color=color, 
            linestyle=linestyle, 
            linewidth=random.random()
            )

# Set plot title, axes labels, and grid lines
ax.set_title(label = '')
ax.grid(color='teal', linestyle='--', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_facecolor('#301934')

# Save the plot as a JPG image
plt.savefig('E:\GitHub\dart\dallery\dart_1.jpg', dpi=600, facecolor='#301934', bbox_inches='tight')

# Close the plot
plt.close()

print("Image saved as 'data_art.jpg'")
