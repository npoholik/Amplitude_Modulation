import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from IPython import display

# To create a sine wave animation:

fig, ax = plt.subplots()

t = np.linspace(0, 2*np.pi, 200)

z = 0

lines_plotted = plt.plot([],color='white')

line = lines_plotted[0]

#Set limits for one full period 
ax.set(xlim=[0, 2*np.pi], ylim=[-1.1, 1.1])

#Remove everything except for the plotted signal itself
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])


def update(frame):
    z = np.sin(t+2*np.pi*frame/200)
    # update the line plot:
    line.set_xdata(t)
    line.set_ydata(z)
    #This will ensure each frame is set at the edge of the graph (for a smooth GIF loop)
    return line

# Looking for a 363 by 103 pixel GIF (1 inch = 100 pixels)
fig.set_figwidth(3.63)
fig.set_figheight(1.03)

#Remove the background:
fig.patch.set_alpha(0)
ax.patch.set_color('#28282B') # Hex:  #28282B

# Generate the animated GIF, and save it using PillowWriter
ani = FuncAnimation(fig=fig, func=update, frames=200, interval=35)
ani.save("Sin.gif", dpi=300, writer=PillowWriter(fps=25))

#Show plot to confirm:
plt.show()





