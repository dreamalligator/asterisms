import skyfield
from .geometry import center, circumcenter
from .cartography import plot
from skyfield.data import hipparcos

__version__ = 0.02

class Constellation(object):
    """A constellation or asterism.

    A `Constellation` instance has the following attributes.

    | `name` - the name of the constellation or asterism.
    | `abbrev` - abbreviation of the constellation.
    | `name_alt` - endonym, colloquial name, or alternative name of constellation.
    | `segs_n` - the number of segments that comprise the constellation.
    | `segs` - a list of star pairs that comprise segments.
    | `center` - a coordinate pair of the center of the constellation.
    | `stars` - a list of stars in the constellation.
    """
    def __init__(self, *args, **kw):
        self.name = kw.pop('name', None)
        self.abbrev = kw.pop('abbrev', None)
        self.name_alt = kw.pop('name_alt', None)
        self.segs = kw.pop('segs', [])
        if(isinstance(self.segs, str)):
            self.segs = self.segs.split()
        if(len(self.segs)%2 != 0):
            print('WARNING: number of stars in segments should be even.')
        self.segs_n = len(self.segs)/2
        self.stars = []
        for star in list(set(self.segs)):
            self.stars.append(hipparcos.get(star))
        self.center = center(self.stars)
        self.circumcenter, self.circumcenter_radius = circumcenter(self.stars)

    def plot(self, projection='mollweide'):
        cartography.plot(self.stars, title=self.name, projection=projection)
        return

    def __repr__(self):
        """Return a useful textual representation of this Constellation."""
        return('<asterism.Constellation name=%s abbrev=%s name_alt=%s segs_n=%s center=%s circumcenter=%s circumcenter_radius=%s>' % (self.name, self.abbrev, self.name_alt, self.segs_n, self.center, self.circumcenter, self.circumcenter_radius))

class Boundary():
    """A boundary for a constellation, asterism, or other celestial object.

    A `Boundary` instance has the following attributes.

    `name` - the name of the boundary
    `points` - a list of celestial coordinate pairs in order for the border;
               closed or unclosed acceptable
    `area` - area of the celestial polygon
    `center` - a coordinate pair of the center of the polygon
    `epoch` - epoch that these coordinates were set by

    """
    def __repr__(self):
        """Return a useful textual representation of this Boundary."""
        return('<asterism.Boundary>')
