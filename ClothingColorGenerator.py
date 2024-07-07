import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

# Define the dimensions of the pattern pieces (example values)
width = 64.0  # inches
length = 1.69 * 36  # yards to inches (1.69 yards * 36 inches per yard)
max_efficiency = 78.62  # percentage
wastage = 21.38  # percentage

# Define the pattern pieces based on the image
# Note: Adjust these dimensions and shapes based on actual measurements from the image
pattern_pieces = {
    'piece_1': [(0, 0), (width * 0.5, 0), (width * 0.5, length * 0.3), (0, length * 0.3)],
    'piece_2': [(width * 0.5, 0), (width, 0), (width, length * 0.3), (width * 0.5, length * 0.3)],
    'piece_3': [(0, length * 0.3), (width * 0.5, length * 0.3), (width * 0.5, length * 0.6), (0, length * 0.6)],
    'piece_4': [(width * 0.5, length * 0.3), (width, length * 0.3), (width, length * 0.6), (width * 0.5, length * 0.6)],
    'piece_5': [(0, length * 0.6), (width * 0.5, length * 0.6), (width * 0.5, length), (0, length)],
    'piece_6': [(width * 0.5, length * 0.6), (width, length * 0.6), (width, length), (width * 0.5, length)],
}

def draw_pattern(pattern_pieces):
    fig, ax = plt.subplots()
    
    colors = ['yellow', 'green', 'blue', 'red', 'purple', 'orange']
    for i, (name, piece) in enumerate(pattern_pieces.items()):
        polygon = Polygon(piece, closed=True, fill=True, edgecolor='black', facecolor=colors[i % len(colors)], label=name)
        ax.add_patch(polygon)
    
    ax.set_aspect('equal')
    plt.xlim(0, width)
    plt.ylim(0, length)
    plt.axis('off')
    plt.legend()
    plt.show()
    
    # Save the pattern as a PDF or SVG
    fig.savefig('regenerated_pattern.pdf')
    fig.savefig('regenerated_pattern.svg')

draw_pattern(pattern_pieces)
