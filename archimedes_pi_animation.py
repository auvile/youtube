import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.animation import FuncAnimation
from matplotlib import animation
import matplotlib.patches as patches

# Function to draw a circle
def draw_circle():
    circle = plt.Circle((0, 0), 1, color='r', fill=False)
    ax.add_patch(circle)

# Function to draw a regular polygon
def draw_polygon(x, y, sides, color):
    theta = np.linspace(0, 2 * np.pi, sides + 1)
    x_vals = np.cos(theta) + x
    y_vals = np.sin(theta) + y
    ax.plot(x_vals, y_vals, 'ko-', markersize=3, linewidth=1, color='white')
    return plt.Polygon(np.column_stack((x_vals, y_vals)), closed=True, color=color, alpha=0.3)

# Function to draw lines from the center to the edges of the polygon
def draw_lines(sides):
    theta = np.linspace(0, 2 * np.pi, sides + 1)[:-1]
    x_vals = np.cos(theta)
    y_vals = np.sin(theta)
    for i in range(sides):
        plt.plot([0, x_vals[i]], [0, y_vals[i]], color='white', linewidth=0.5)

# Number of sides for the initial polygons
sides = 3

# Initialize the animation parameters
steps = 100
interval=0
base_interval = 1500
speed_change_rate = 200

# Initialize the plot with a larger figure size
fig, ax = plt.subplots(figsize=(8, 8))

# Set plot limits and aspect ratio
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')

# Set background color to black
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Remove axis label and values
ax.set_xticks([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_yticklabels([])

# Animation function
def animate(i):
    ax.clear()
    if i > steps * 0.2:
        draw_circle()

    # Update the number of sides
    current_sides = sides + i

    perimeter_formula = r'$P_n = 2n \cdot \sin\left(\frac{{\pi}}{{n}}\right)$'
    pi_formula = r'$\pi \approx \frac{{P_n}}{{2}}$'

    inscribed_perimeter = current_sides * np.sin(np.pi / current_sides)
    perimeter_calc = '$P_{} = 2 \\times {} \\times \\sin\\left(\\frac{{\pi}}{{{}}}\\right) = {:.5f}$'.format(current_sides, current_sides, current_sides, inscribed_perimeter)

    # Step 5: Use the inscribed perimeter to estimate pi
    estimated_pi = inscribed_perimeter / 2
    pi_calc = '$\\pi \\approx \\frac{{ {:.5f} }}{{2}} = {:.5f}$'.format(inscribed_perimeter, estimated_pi)

    polygon = draw_polygon(0, 0, current_sides, 'r')

    # Draw lines from the center to the polygon edges
    draw_lines(current_sides)

    # Calculate the coordinates of the midpoint between the edges of the polygon
    intersection_x = 0.5 * (np.cos(0) + np.cos(2 * np.pi / current_sides))
    intersection_y = 0.5 * (np.sin(0) + np.sin(2 * np.pi / current_sides))

    # Add a line from the center to the intersection point
    ax.plot([0, intersection_x], [0, intersection_y], color='white', linestyle='dashed', linewidth=1)

    # Add a dot at the intersection point
    ax.plot(intersection_x, intersection_y, 'ro')

    # Set plot limits and aspect ratio
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')

    additional_dot_x = np.cos(2 * np.pi / current_sides)
    additional_dot_y = np.sin(2 * np.pi / current_sides)

    # Coordinates for the triangle
    triangle_coords = np.array([[0, 0], [intersection_x, intersection_y], [1, 0]])

    # Create a polygon patch for the triangle
    triangle_patch = patches.Polygon(triangle_coords, closed=True, color='lightblue', alpha=0.3)
    ax.add_patch(triangle_patch)
    

    # Add an angle sign close to the center
    angle_sign = patches.Wedge((0, 0), 0.1, 1, 360 / current_sides / 2, width=0.1, alpha=0.5, color='orange')
    ax.add_patch(angle_sign)

    # Calculate the centroid of the triangle
    centroid_x = (np.cos(0) + np.cos(2*np.pi/current_sides) + 0) / 3
    centroid_y = (np.sin(0) + np.sin(2*np.pi/current_sides) + 0) / 3

    # Add a label at the centroid of the triangle
    ax.text(centroid_x, centroid_y, r"$\theta$", fontsize=12, color="white", ha='center', va='center')

    # Display the current step and the estimated value of pi
    # ax.set_title(f'Step {i}, Estimated value of pi: {estimated_pi:.5f}', color='white')
    # ax.text(0, -1.3, perimeter_formula, fontsize=12, ha='center', color='white')
    # ax.text(0, -1.4, pi_formula, fontsize=12, ha='center', color='white')
    # ax.text(0, -1.5, perimeter_calc, fontsize=12, ha='center', color='white')
    # ax.text(0, -1.6, pi_calc, fontsize=12, ha='center', color='white')

    # Gradually adjust the animation speed (not working)
    interval = base_interval - speed_change_rate * i
    if interval < 100:
        interval = 100
    print("interval", interval)
    ani.event_source.interval = interval

# Create the animation
ani = FuncAnimation(fig, animate, frames=steps,repeat=False)

# Writer = animation.writers['ffmpeg']
# writer = Writer(fps=30, metadata=dict(artist='Me'), bitrate=2000)
# ani.save('archimedes_pi_animation.mp4', writer=writer, dpi=300)

# Show the animation
plt.show()
