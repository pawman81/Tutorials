import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

"""
source:
https://stackoverflow.com/questions/22010586/matplotlib-animation-duration

For the saved animation the duration is going to be frames * (1 / fps) (in seconds)
For the display animation the duration is going to be frames * interval / 1000 (in seconds)

Saving animation:

writervideo = animation.FFMpegWriter(fps=30)
anim.save('blah.mp4', writer=writervideo)
"""

def savevideo():
    print('saving...')
    writervideo = animation.FFMpegWriter(fps=60,)
    anim.save('blah.mp4', writer=writervideo)
    print('done...')


def animate(i):
    par1 = i/10
    par2 = i/20
    par3 = i/4
    point1.set_data(np.sin(par1), np.cos(par1))
    point2.set_data(2*np.sin(par2),2*np.cos(par2))
    point3.set_data(5*np.sin(par3), 5*np.cos(par3))
    text1.set_text(f'timestep: {i}')
    text2.set_text(f'{i/np.pi}')

fig, (ax, ax2) = plt.subplots(nrows=2, ncols=1)
point1, = ax.plot(0, 0, 'go', label = 'normal')
point2, = ax.plot(0, 0, 'ro', label = 'lazy')
point3, = ax.plot(0, 0, 'bo', label = 'fast')
text1 = ax.text(-8,8, 'timestep: 0')
text2 = ax2.text(2,2, ' Hmmm')

radii = [1,2,5]
circles = [plt.Circle((0,0), radius=r, fill=False, linestyle='dotted', alpha = 0.7) for r in radii]
for circle in circles:
    ax.add_patch(circle)
ax.plot(0,0, marker = 'o', color = 'orange', markersize = 10)
ax.plot()

ax.legend()
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)

ax2.set_xlim(0,4)
ax2.set_ylim(0,4)
anim = animation.FuncAnimation(fig,
                     animate,
                     frames = 1800,
                     interval= 30,
                     repeat= True,
                     )

# savevideo()
plt.show()


