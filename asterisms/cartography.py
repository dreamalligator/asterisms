import matplotlib.pyplot as plt
import skyfield

def init_plot(figsize=(8,6)):
    return plt.subplots(1,figsize=figsize)

def plot(stars, ax=None, g=True, title=None, projection='mollweide', color='blue'):
    '''A simple plotting helper function.

    Valid projection values are ``mollweide``, ``lambert``, ``hammer``, and ``aitoff``. Passing `None` gives an equirectangular projection.

    Defaults are ``projection='mollweide'``, ``title=None``, ``g=True`` (grid), ``color='blue'``, ``ax=None``.

    Given a list of stars, or a list of position tuples.

    Returns plot.
    '''

    if(not isinstance(stars, list)):
        raise ValueError('Must be passed a list of Stars or a list of position tuples.')
        return None

    # if(ax is None):
    #     ax = plt.gca()
    ax = plt.gca(projection=projection)
    ax.grid(g)
    ra_list = []
    dec_list = []
    if(isinstance(stars[0], skyfield.starlib.Star)):
        for i in range(len(stars)):
            ra_list.append(stars[i].ra.radians)
            dec_list.append(stars[i].dec.radians)
    else:
        for i in range(len(stars)):
            ra_list.append(stars[i][0].radians)
            dec_list.append(stars[i][1].radians)
    my_plot = ax.scatter(ra_list, dec_list, color=color)
    ax.set_xticklabels(['14h','16h','18h','20h','22h','0h','2h','4h','6h','8h','10h'])
    if(title!=None):
        plt.title(title)
    return my_plot

def plot_circle(center=None, radius=None, ax=None, clip_on=True, alpha=1.0, facecolor='none', edgecolor='black', lw=1, projection='mollweide'):
    if(center is None or radius is None):
        raise ValueError('Need to specify a center position tuple and radius.')
        return
    if ax is None:
        ax = plt.gca()
    ax = plt.gca(projection=projection)
    if(isinstance(center[0], skyfield.units.Angle)):
        center = (center[0].radians,center[1].radians)
        radius = radius.radians
    circle=plt.Circle(center, radius, clip_on=clip_on, facecolor=facecolor, alpha=alpha, edgecolor=edgecolor, lw=lw)
    my_plot = ax.add_artist(circle)
    return my_plot
