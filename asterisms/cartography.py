from pylab import *
import matplotlib.pyplot as plt
import skyfield

def plot(stars, projection='mollweide', title=None, g=True, figsize=(8,6)):
    '''A simple plotting helper function.

    Valid projection values are ``mollweide``, ``lambert``, ``hammer``, and ``aitoff``.

    Defaults are ``projection='mollweide'``, ``title=None``, ``g=True`` (grid).

    Given a list of stars, or a list of position tuples.

    Returns nothing.
    '''
    #TODO PROJECTIONS
    #* https://en.wikipedia.org/wiki/Lambert_conformal_conic_projection
    #* https://en.wikipedia.org/wiki/Lambert_cylindrical_equal-area_projection
    #* https://en.wikipedia.org/wiki/Lambert_azimuthal_equal-area_projection

    if(not isinstance(stars, list)):
        raise ValueError('Must be passed a list of Stars or a list of position tuples.')
        return None

    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection=projection)

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
    ax.scatter(ra_list, dec_list)
    ax.set_xticklabels(['14h','16h','18h','20h','22h','0h','2h','4h','6h','8h','10h'])
    if(title!=None):
        plt.title(title)
    grid(g)
    show()
    return
