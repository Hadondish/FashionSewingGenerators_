import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw_tshirt_pattern(chest, waist, hip, length, sleeve_length):
    fig, ax = plt.subplots()
    
    # Simplified calculations for pattern pieces
    front_piece = [
        (0, 0),  # bottom left
        (waist / 4, 0),  # bottom right
        (chest / 4, length),  # top right
        (0, length),  # top left
        (0, 0)  # closing the loop
    ]
    
    back_piece = [
        (waist / 4 + 2, 0),  # bottom left
        (waist / 2, 0),  # bottom right
        (chest / 2, length),  # top right
        (waist / 4 + 2, length),  # top left
        (waist / 4 + 2, 0)  # closing the loop
    ]
    
    front_sleeve = [
        (0, 0),  # bottom left
        (sleeve_length / 2, 0),  # bottom right
        (sleeve_length / 2, sleeve_length / 4),  # top right
        (0, sleeve_length / 4),  # top left
        (0, 0)  # closing the loop
    ]
    
    back_sleeve = [
        (sleeve_length / 2 + 2, 0),  # bottom left
        (sleeve_length, 0),  # bottom right
        (sleeve_length, sleeve_length / 4),  # top right
        (sleeve_length / 2 + 2, sleeve_length / 4),  # top left
        (sleeve_length / 2 + 2, 0)  # closing the loop
    ]
    
    ax.add_patch(Polygon(front_piece, closed=True, fill=None, edgecolor='b'))
    ax.add_patch(Polygon(back_piece, closed=True, fill=None, edgecolor='r'))
    ax.add_patch(Polygon(front_sleeve, closed=True, fill=None, edgecolor='g'))
    ax.add_patch(Polygon(back_sleeve, closed=True, fill=None, edgecolor='y'))
    
    ax.set_aspect('equal')
    plt.xlim(-5, chest / 2 + 5)
    plt.ylim(-5, length + 5)
    plt.axis('off')
    plt.show()
    
    # Save the pattern as a PDF or SVG
    fig.savefig('tshirt_pattern.pdf')
    fig.savefig('tshirt_pattern.svg')

# Example measurements
chest = 100  # cm
waist = 90  # cm
hip = 100  # cm
length = 70  # cm
sleeve_length = 30  # cm


draw_tshirt_pattern(chest, waist, hip, length, sleeve_length)