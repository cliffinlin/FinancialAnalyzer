import matplotlib.pyplot as plt
import numpy as np

def plot_figures(figures, nrows = 1, ncols=1):
    """Plot a dictionary of figures.

    Parameters
    ----------
    figures : <title, figure> dictionary
    ncols : number of columns of subplots wanted in the display
    nrows : number of rows of subplots wanted in the figure
    """

    fig, axeslist = plt.subplots(ncols=ncols, nrows=nrows)
    for ind,title in enumerate(figures):
        axeslist.ravel()[ind].imshow(figures[title], cmap=plt.gray())
        axeslist.ravel()[ind].set_title(title)
        axeslist.ravel()[ind].set_axis_off()
    plt.tight_layout() # optional
    plt.show()

# generation of a dictionary of (title, images)
number_of_im = 6
figures = {'im'+str(i): np.random.randn(100, 100) for i in range(number_of_im)}

# plot of the images in a figure, with 2 rows and 3 columns
plot_figures(figures, 2, 3)