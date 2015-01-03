import skyfield
from skyfield.units import Angle, Distance
import numpy as np
from numpy import array
from asterisms.welzl import *

#https://en.wikipedia.org/wiki/Machine_epsilon
#epsilon = np.finfo(float).eps
epsilon = 1e-15

def midpoint(p1, p2):
    '''The midpoint between two celestial coordinates.

    Given a point as a tuple of either ``(Ra, Dec)`` or ``(Ra, Dec, Dist)``.
    RA is of Skyfield type Angle, with ``preference='hours'``. Dec is of Skyfield
    type Angle. Distance is Skyfield type Distance, in AU units.

    If dist is included, the returned tuple is (Mid_RA, Mid_Dec, Mid_Dist).
    Otherwise, it is (Mid_RA, Mid_Dec).

    You can alternatively use ``center`` for multiple points.'''

    if(not isinstance(p1, tuple) or not isinstance(p2, tuple)):
        raise ValueError('Can only pass two tuples to this function.')
        return None

    mean_ra = (p1[0].radians + p2[0].radians) / 2.0
    mean_dec = (p1[1].radians + p2[1].radians) / 2.0
    if(len(p1) == 3 and len(p2) == 3):
        mean_dist = (p1[2].AU + p2[2].AU) / 2.0
        return (Angle(radians=mean_ra, preference='hours'), Angle(radians=mean_dec, signed=True), Distance(AU=mean_dist))
    else:
        return (Angle(radians=mean_ra, preference='hours'), Angle(radians=mean_dec, signed=True))

def center(positions):
    '''Calculate the visual center of a list of coordinates.

    This function can take two kinds of lists of positions. Lists of tuples, or
    lists of Stars.

    This may be useful for automatically centering a telescope or for a program
    that automatically zooms to a location.

    The first is a list of coordinates in tuples. It looks like ``[(ra0,dec0), (ra1,dec1)]``,
    where RA and Dec are Skyfield Angle instances.

    ::

        import skyfield
        from skyfield.api import Star, earth, now
        from skyfield.units import Angle, Distance
        from numpy import array

        algol = Star(ra_hours=( 3,  8, 10.1315),  dec_degrees=(40, 57, 20.332))  #approximately Algol
        mizar = Star(ra_hours=(13, 23, 55.5),     dec_degrees=(54, 55, 31))      #approximately Mizar
        vega  = Star(ra_hours=(18, 36, 56.33635), dec_degrees=(38, 47, 01.2802)) #approximately Vega
        stars = [algol, mizar, vega]
        positions = []
        for star in stars:
            star_pos = earth(now()).observe(star)
            positions.append(star_pos.radec())

        center1 = a.center(positions)

    Additionally, you can pass it a list of Stars. For example with Alcor, Mizar and Dubhe.

    ::

        from skyfield.data import hipparcos
        stars = []
        stars.append(hipparcos.get('65477'))
        stars.append(hipparcos.get('65378'))
        stars.append(hipparcos.get('54061'))
        center3 = center(stars)

    RA is of Skyfield type Angle, with ``preference='hours'``. Dec is of Skyfield
    type Angle.

    Returns a coordinate tuple of right ascension and declination ``(ra,dec)``.'''

    if(not isinstance(positions, list)):
        raise ValueError('Must be passed a list.')
        return None

    # Average the coordinates to get an unweighted center
    mean_ra = Angle(hours=0.0).radians
    mean_dec = Angle(degrees=0.0).radians
    # Passed list of Stars
    if(isinstance(positions[0], skyfield.starlib.Star)):
        for star in positions:
            mean_ra = mean_ra + star.ra.radians
            mean_dec = mean_dec + star.dec.radians
    # Or passed list of position tuples
    else:
        for coord in positions:
            mean_ra = mean_ra + coord[0].radians
            mean_dec = mean_dec + coord[1].radians
    mean_ra = mean_ra / len(positions)
    mean_dec = mean_dec / len(positions)

    ctr = (Angle(radians=mean_ra, preference='hours'), Angle(radians=mean_dec, signed=True))
    return ctr

def circumcenter(positions):
    '''Calculate the circumcenter of a list of coordinates.

    Given a list of position tuples, ``[(ra0, dec0), (ra1, dec1)]`` or a list of Stars.

    Returns a position tuple of right ascension and declination ``(ra,dec)``.

    This may be useful for automatically centering a telescope or for a program that automatically zooms to a location.

    The algorithm used is based on Emo Welzl's paper [#]_ which solves this problem in O(n) time. See `smallest-circle problem <https://en.wikipedia.org/wiki/Smallest-circle_problem>`_.

    .. [#]  Welzl, Emo (1991), "`Smallest enclosing disks (balls and ellipsoids) <http://dx.doi.org/10.1007%2FBFb0038202>`_", in Maurer, H., New Results and New Trends in Computer Science, Lecture Notes in Computer Science 555, Springer-Verlag, pp. 359-370'''

    if(not isinstance(positions, list)):
        raise ValueError('Must be passed a list of Stars or a list of position tuples.')
        return None

    md = Minidisk(points = positions)
    return md.center, md.radius

class Minidisk(object):
    '''Calculate smallest enclosing disk. This computes the smallest enclosing disk of a set of n points in the plane in expected O(n) time.

    Given a set P of n points.

    Returns the closed disk of smallest radius containning all points in P. The values returned are a tuple of center, and the radius.

    The algorithm used is based on Emo Welzl's paper [#]_ which solves this problem in O(n) time. See `smallest-circle problem <https://en.wikipedia.org/wiki/Smallest-circle_problem>`_.

    .. [#]  Welzl, Emo (1991), "`Smallest enclosing disks (balls and ellipsoids) <http://dx.doi.org/10.1007%2FBFb0038202>`_", in Maurer, H., New Results and New Trends in Computer Science, Lecture Notes in Computer Science 555, Springer-Verlag, pp. 359-370

    A functionality I added is that you can initialize a minidisk with *both* a center, radius *and* a list of points. The reason for this is if you wanted to start off with a circle, but expand it to include the extra points using Welzl's algorithm.

    If simply passed a center and radius, with no points, then this is just a circle and nothing is computed. It will return the center and radius. If not an Angle, then forced to float type.

    If passed only a list of positions, then the minimum enclosing circle is computed using Welzl's algorithm.'''

    # This option allows the circle to be initialized by passing a center and radius to the function.
    allow_initial_circle = True

    def __init__(self, *args, **kw):
        '''Initialize an instance of the Minidisk class'''
        self.points = kw.pop('points', None)
        #self.p = kw.pop('p', None)
        if(Minidisk.allow_initial_circle):
            self.radius = kw.pop('radius', Angle(radians = 0.0))
            self.center = kw.pop('center', (None, None))
            # If not an Angle, then ensure float
            if(not isinstance(self.radius, skyfield.units.Angle)):
                self.radius = float(self.radius)
            if(self.center[0] is not None and not isinstance(self.center[0], skyfield.units.Angle)):
                self.center = (float(self.center[0]), float(self.center[1]))
        else:
            self.radius = Angle(radians = 0.0)
            self.center = (None, None)
        self.ra = self.center[0]
        self.dec = self.center[1]
        if(self.points is None):
            self.format = None
            print('WARNING: This instance was not created with any points to be fed to Welzl\'s algorithm. If initialized with a center and radius, it will return the same circle with float types. If not, then it will return a bare circle, with no center and a radius of zero.')
        else:
            if(isinstance(self.points[0], tuple)):
                self.format = type(self.points[0][0])
            else:
                self.format = type(self.points[0])
            print('type is {}'.format(self.format))
            self.calc()

    def calc(self):
        (ra, dec, radius) = make_circle(self.points)
        if(isinstance(self.format, (type(skyfield.starlib.Star), type(skyfield.units.Angle)))):
            print('yes! star')
            self.ra = Angle(radians = ra, preference='hours')
            self.dec = Angle(radians = dec, signed=True)
            self.radius = Angle(radians = radius)
        else:
            print('no! not angle')
            self.ra = ra
            self.dec = dec
            self.radius = radius
        self.center = (self.ra, self.dec)
        return

    def __repr__(self):
        """Return a useful textual representation of this Minidisk."""
        return('<asterism.geometry.Minidisk center=%s radius=%s>' % (self.center, self.radius))

def linear_interpolate(x0,y0,x1,y1,x=None,y=None):
    '''Linearly interpolate between two points. If not passed any x or y, assume want bisection pt.'''
    if(x==None and y==None):
        x=(x0+x1)/2.
        y=(y0+y1)/2.
    elif(y==None):
        y=y0+(y1-y0)*(x-x0)/(x1-x0)
    elif(x==None):
        x=x0+(x1-x0)*(y-y0)/(y1-y0)
    return x,y
