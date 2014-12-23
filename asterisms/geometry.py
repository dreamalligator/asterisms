from skyfield.units import Angle, Distance
import numpy as np
from numpy import array

def midpoint(p1, p2):
    '''The midpoint between two celestial coordinates.

    Given a point as a tuple of either ``(Ra, Dec)`` or ``(Ra, Dec, Dist)``.
    RA is of Skyfield type Angle, with ``preference='hours'``. Dec is of Skyfield
    type Angle. Distance is Skyfield type Distance, in AU units.

    If dist is included, the returned tuple is (Mid_RA, Mid_Dec, Mid_Dist).
    Otherwise, it is (Mid_RA, Mid_Dec).

    You can alternatively use ``barycenter`` for multiple points.'''

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

def barycenter(position, weight=None):
    '''Calculate the barycenter of a list of coordinates.

    This function can take a few different forms of position.

    The first is a list of coordinates in tuples in the form ``[(ra0,dec0,dist0), (ra1,dec1,dist1)]``.
    You can also pass it an numpy array of such a list such as if ``position_list = [(ra0,dec0,dist0), (ra1,dec1,dist1)]`` then you
    can pass it array(position_list) which looks like

    ::

        [[(ra0,dec0,dist0)]
         [(ra1,dec1,dist1)]]``

    Additionally, you can pass it a list of Stars. For example with Alcor, Mizar and Dubhe.

    ::

        from skyfield.data import hipparcos
        stars = []
        stars.append(hipparcos.get('65477'))
        stars.append(hipparcos.get('65378'))
        stars.append(hipparcos.get('54061'))
        center = barycenter(stars)

    RA is of Skyfield type Angle, with ``preference='hours'``. Dec is of Skyfield
    type Angle. Distance is Skyfield type Distance, in AU units.

    Optionally,
    given the option to weight by magnitude with ``weight=True``.

    Returns a coordinate tuple of right ascension and declination ``(ra,dec)``.

    The default is to assume that all objects are equally weighted.

    An alternative is to use a magnitude weighted barycenter.

    This may be useful for automatically centering a telescope or for a program
    that automatically zooms to a location.'''

    if(isinstance(position, list)):
        position_array = array(position)
    elif(isinstance(position, np.ndarray)):
        position_array = position # Already a numpy array
    else:
        raise ValueError('Must be passed an array or list.')
        return None

    if(weight):
        print('WARNING: IGNORING WEIGHT PARAMETER, NOT SET UP YET.')

    # Average the coordinates to get an unweighted center
    mean_ra = Angle(hours=0.0).radians
    mean_dec = Angle(degrees=0.0).radians
    mean_dist = Distance(AU=0.0).AU
    for coord in position_array:
        mean_ra = mean_ra + coord[0].radians
        mean_dec = mean_dec + coord[1].radians
        mean_dist = mean_dist + coord[2].AU
    mean_ra = mean_ra / len(position_array)
    mean_dec = mean_dec / len(position_array)
    mean_dist = mean_dist / len(position_array)

    center = (Angle(radians=mean_ra, preference='hours'), Angle(radians=mean_dec, signed=True), Distance(AU=mean_dist))
    return center

# def slope(p1, p2):
#     '''The slope between two points
#
#     Given two points as tuples. If a third distance coord is passed, it is
#     ignored.
#
#     Returns the slope as delta-Dec/delta-RA in radians.
#
#     This is simply a visual slope helper function.'''
#
#     if(not isinstance(p1, tuple) or not isinstance(p2, tuple)):
#         raise ValueError('Can only pass two tuples to this function.')
#         return None
#
#     m = (p1[1].radians - p2[1].radians)/(p1[0].radians - p2[0].radians)
#     return m

# def circumcenter(position):
#     '''Calculate the circumcenter of a list of coordinates.
#
#     Given a list of coordinates in tuples, ``[(x0,y0), (x1,y1)]``. It may have
#     a third Distance coord in the tuple, but it is thrown away, because the
#     circumcenter returned is simply a visual circumcenter.
#
#     Returns a coordinate tuple of right ascension and declination ``(ra,dec)``.
#
#     This may be useful for automatically centering a telescope or for a program
#     that automatically zooms to a location.
#
#     Typically, when you have three points, the point where the perpendicular
#     bisectors of a triangle meet is called the circumcenter. It lies inside for
#     and acute, and outside for an obtuse, and at the center of the hypotenuse
#     for a right triangle.
#
#     To decide the three points, my algorithm chooses the furthest point from the
#     visual barycenter to begin (just using RA and Dec, ignoring distance). We
#     can call this point A. The second point is then chosen for being the
#     furthest point away from point A. This is point B.
#
#     These steps seem like a good course, but I am going to have to math-out
#     whether these choices cover every possible sets of scattered data. We then
#     are going to choose the midpoint between A and B, and call this D. Point C,
#     the third point of the descriptive triangle, is then the furthest point away
#     from this midpoint D that is not A or B.'''
#
#     if(isinstance(position, list)):
#         position_array = array(position)
#     elif(isinstance(position, np.ndarray)):
#         position_array = position # Already a numpy array
#     else:
#         raise ValueError('Must be passed an array or list.')
#         return None
#
#     # Get point A
#     A =
#     # Get point B
#     B =
#     # Get point C
#     C =
#
#     # Get all the midpoints
#     mp_AB = midpoint(A,B)
#     mp_BC = midpoint(B,C)
#     mp_CA = midpoint(C,A)
#
#     # Calculate slope of the perpendicular bisector of the lines AB, BC, and CA;
#     # ie, the negative reciprocal of the slope.
#
#     # Regular slopes, returned as radians
#     m_AB = slope(A,B)
#     m_BC = slope(B,C)
#     m_CA = slope(C,A)
#     print('doublecheck that i can use radians here, and get reciprocal of radian??')
#     # Perpendicular bisector slopes
#     m_pb_AB = -1.0 / m_AB
#     m_pb_BC = -1.0 / m_BC
#     m_pb_CA = -1.0 / m_CA
#
#     ra = skyfield.units.Angle(hours=0.0)
#     dec = skyfield.units.Angle(degrees=0.0)
#     return ra, dec
