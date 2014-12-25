import skyfield
from skyfield.units import Angle, Distance
#from skyfield.starlib import Star
import numpy as np
from numpy import array

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

def circumcenter(position):
    '''Calculate the circumcenter of a list of coordinates.

    Given a list of position tuples, ``[(ra0, dec0), (ra1, dec1)]`` or a list of Stars.

    Returns a position tuple of right ascension and declination ``(ra,dec)``.

    This may be useful for automatically centering a telescope or for a program that automatically zooms to a location.

    The algorithm used is basd on Emo Welzl's paper Smallest enclosing disks (balls and ellipsoids) (1991) which solves this problem in O(n) time.
    '''

    if(not isinstance(position, list)):
        raise ValueError('Must be passed a list of Stars or a list of position tuples.')
        return None

    cc_ra = Angle(hours=0.0).radians
    cc_dec = Angle(degrees=0.0).radians
    return cc_ra, cc_dec
