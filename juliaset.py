import matplotlib.pyplot as plt
import math
import numpy as np
import matplotlib.cm as cm
import cmath


def f(z, c):
    return z**2 + c

print(cmath.sin(complex(1,1)))

# Image width and height; parameters for the plot
im_width, im_height = 500, 500
c = -1
radius = (1 + math.sqrt(1+4*abs(c)))/2
nit_max = 1000
xmin, xmax = -3, 3
xwidth = xmax - xmin
ymin, ymax = -3, 3
yheight = ymax - ymin

julia = np.zeros((im_width, im_height))
for i in range(im_width):
    for j in range(im_height):
        z = complex(i / im_width * xwidth + xmin,
                    j / im_height * yheight + ymin)
        nit = 0
        while abs(z) < radius and nit_max > nit:
            z = f(z, c)
            nit += 1

        shade = 1 - np.sqrt(nit / nit_max)
        ratio = nit / nit_max
        julia[i, j] = ratio

fig, ax = plt.subplots()
ax.imshow(np.transpose(julia), interpolation='nearest', cmap=cm.hot)
# Set the tick labels to the coordinates of z0 in the complex plane
xtick_labels = np.linspace(xmin, xmax, round(xwidth * 2))
ax.set_xticks([(x-xmin) / xwidth * im_width for x in xtick_labels])
ax.set_xticklabels(['{:.1f}'.format(xtick) for xtick in xtick_labels])
ytick_labels = np.linspace(ymin, ymax, round(yheight * 2))
ax.set_yticks([(y-ymin) / yheight * im_height for y in ytick_labels])
ax.set_yticklabels(['{:.1f}'.format(ytick) for ytick in ytick_labels])
plt.show()
