import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# To create a sine wave animation:

fig, ax = plt.subplots()

#Initial values
t = np.linspace(0, 2*np.pi, 32)
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

#Create function to update the frames of the plot
def update(frame):
    z = np.sin(t+2*np.pi*frame/32)
    # Update the line plot:
    #This will ensure each frame is set at the edge of the graph (for a smooth GIF loop)
    line.set_xdata(t)
    line.set_ydata(z)
    return line

# Looking for a 363 by 103 pixel GIF (1 inch = 100 pixels)
# -> Numbers had to be tweaked to fit the GUI, not a perfect 1:1 
fig.set_figwidth(1.615)
fig.set_figheight(0.455)

#Remove the background:
fig.patch.set_alpha(0)
ax.patch.set_color('#28282B') # Hex:  #28282B (matches background of GUI, setting 'none' causes GIF to melt??)

# Generate the animated GIF, and save it using PillowWriter
ani = FuncAnimation(fig=fig, func=update, frames=32, interval=35)
ani.save("Sin.gif", dpi=300, writer=PillowWriter(fps=25))

#Show plot to confirm:
plt.show()





