import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters
plot_min = 0
plot_max = 2

num_terms = 8
base_length = 1

# Create the figure and axis
fig, ax = plt.subplots()

ax.set_facecolor((255/255, 255/255, 225/255))

ax.set_aspect('equal')
plt.xticks([])
plt.yticks([])

for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(2)
    spine.set_color('black')

# Function to update the plot for each step of the animation
def update(i):
    x = 0
    y = 0
    area = 1
    for j in range(i + 1):
        length = base_length / (2 ** j)
        rect = plt.Rectangle((x, y), length, length, linewidth=1, edgecolor='black', facecolor=(211/255, 170/255, 255/255), alpha=0.6)
        ax.add_patch(rect)
        x += length
        y += length
        area /= 4
        if j < 3:
            ratio = "1/${" + str(2**(j+1)) + "}$"
            plt.text(y - length - 0.1, y - length / 2, ratio, horizontalalignment='center', verticalalignment='center', fontsize=10)
            plt.text(y - length / 2, y - length - 0.1, ratio, horizontalalignment='center', verticalalignment='center', fontsize=10)
        plt.hlines(y=x, xmin=x, xmax=plot_max, colors='black', alpha=0.5, linewidth=1)
        plt.vlines(x=y, ymin=y, ymax=plot_max, colors='black', alpha=0.5, linewidth=1)
    plt.xlim(plot_min, plot_max)
    plt.ylim(plot_min, plot_max)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_terms, repeat=False)

# Save animation as a video
# Writer = animation.writers['ffmpeg']
# writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save('geometric_series_animation.mp4', writer=writer)

# Show the animation
plt.show()
