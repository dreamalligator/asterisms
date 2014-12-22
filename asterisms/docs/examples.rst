
Examples
========

Asterisms is intended to aid in logging of historical asterisms.
Whenever possible, I am going to follow conventions of parallel projects
so that there is the utmost compatibility possible. I think usage and
facilitating sharing of information is a big part of the project. To
that end, some of these examples show how to accomplish the equivalent
*without* Asterisms. This could be helpful, if you don't want an extra
dependency. It could also help you seamlessly drop in the Asterisms
project.

.. code:: python

    import asterisms as a
    print('using Asterisms version %s' % a.__version__)

.. parsed-literal::

    using Asterisms version 0.02


Format
------

A note on format and compatibility. Constellation/asterism format is
historically based on the Stellarium (who else uses it?)
``constellationship.fab`` files. See the R.A. Rey asterism files for
example. The other asterism format I chose, was because I didn't see a
point in having two files, when you could have one text file.

Whenever possible, I am deferring position, units, and vector format
decisions to the Skyfield project, which I am going to leverage.

.. code:: python

    import skyfield
    print('using Skyfield version %s' % skyfield.__version__)

.. parsed-literal::

    using Skyfield version 0.4


Barycenter
----------

This example shows how to calculate the barycenter (equally weighted) of
a list of stars with both Skyfield and Asterisms. This could be useful
if you wanted to point a telescope, or a celestrial mapping program, to
the center of a constellation. I like to think of it as a visual
barycenter.

.. code:: python

    import skyfield
    from skyfield.api import Star, earth, now
    from skyfield.units import Angle, Distance
    from numpy import array
    
    # Gather star positions and put coords in an array
    algol = Star(ra_hours=( 3,  8, 10.1315),  dec_degrees=(40, 57, 20.332))  #approximately Algol
    mizar = Star(ra_hours=(13, 23, 55.5),     dec_degrees=(54, 55, 31))      #approximately Mizar
    vega  = Star(ra_hours=(18, 36, 56.33635), dec_degrees=(38, 47, 01.2802)) #approximately Vega
    stars = [algol, mizar, vega]
    positions = []
    for star in stars:
        star_pos = earth(now()).observe(star)
        positions.append(star_pos.radec())
    position_array = array(positions)
    print('Array of Positions')
    print(position_array)

.. parsed-literal::

    Array of Positions
    [[<Angle 03h 08m 10.13s> <Angle +40deg 57' 20.3"> <Distance 2.06265e+14 AU>]
     [<Angle 13h 23m 55.50s> <Angle +54deg 55' 31.0"> <Distance 2.06265e+14 AU>]
     [<Angle 18h 36m 56.34s> <Angle +38deg 47' 01.3"> <Distance 2.06265e+14 AU>]]


How to get the visual Barycenter just using Skyfield

.. code:: python

    # Average the coordinates to get an unweighted center
    mean_ra = skyfield.units.Angle(hours=0.0).radians
    mean_dec = skyfield.units.Angle(degrees=0.0).radians
    mean_dist = skyfield.units.Distance(AU=0.0).AU
    for coord in position_array:
        mean_ra = mean_ra + coord[0].radians
        mean_dec = mean_dec + coord[1].radians
        mean_dist = mean_dist + coord[2].AU
    mean_ra = mean_ra / len(position_array)
    mean_dec = mean_dec / len(position_array)
    mean_dist = mean_dist / len(position_array)
    
    center = (Angle(radians=mean_ra, preference='hours'), Angle(radians=mean_dec, signed=True), Distance(AU=mean_dist))
    print('Center of Array of Positions:')
    print(center)

.. parsed-literal::

    Center of Array of Positions:
    (<Angle 11h 43m 00.66s>, <Angle +44deg 53' 17.5">, <Distance 2.06265e+14 AU>)


And the equivalent using Asterisms.

.. code:: python

    a.barycenter(position_array)



.. parsed-literal::

    (<Angle 11h 43m 00.66s>, <Angle +44deg 53' 17.5">, <Distance 2.06265e+14 AU>)



Visual barycenter of a constellation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    uma = a.Constellation(name='Ursa Major',name_alt='Big Dipper',abbrev='UMA',segs=[])
    print(uma.barycenter)
Circumcenter
------------

This example shows how to calculate the circumcenter of a list of stars
with both Skyfield and Asterisms.


and the equivalent using Asterisms


Hipparcos
---------

At the time of writing, all of the constellations are (to oversimplify
the format) just lists of star segments. Each star is listed by the
Hipparcos number. The only reason I chose this nomenclature is because
others were already using HIP numbers in their constellationship.fab
files. Here is how to set up a constellation just using Skyfield, then
also using Asterisms.

.. code:: python

    #from skyfield.data import hipparcos
    #Alcor is HIP 65477
    #Mizar is HIP 65378
    
    #hipparcos.get(['65477','65378'])

.. code:: python

    line = 'H|       11767| |02 31 47.08|+89 15 50.9| 1.97|1|H|037.94614689|+89.26413805| |   7.56|   44.22|  -11.74|  0.39|  0.45|  0.48|  0.47|  0.55|-0.16| 0.05| 0.27|-0.01| 0.08| 0.05| 0.04|-0.12|-0.09|-0.36|  1| 1.22| 11767| 2.756|0.003| 2.067|0.003| | 0.636|0.003|T|0.70|0.00|L| | 2.1077|0.0021|0.014|102| | 2.09| 2.13|   3.97|P|1|A|02319+8915|I| 1| 1| | | |  |   |       |     |     |    |S| |P|  8890|B+88    8 |          |          |0.68|F7:Ib-IIv SB|G\n'
    star = hipparcos.parse(line)
    print(star.ra.hours, star.dec.degrees)

::


    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)

    <ipython-input-6-5ef0a2152a8b> in <module>()
          1 line = 'H|       11767| |02 31 47.08|+89 15 50.9| 1.97|1|H|037.94614689|+89.26413805| |   7.56|   44.22|  -11.74|  0.39|  0.45|  0.48|  0.47|  0.55|-0.16| 0.05| 0.27|-0.01| 0.08| 0.05| 0.04|-0.12|-0.09|-0.36|  1| 1.22| 11767| 2.756|0.003| 2.067|0.003| | 0.636|0.003|T|0.70|0.00|L| | 2.1077|0.0021|0.014|102| | 2.09| 2.13|   3.97|P|1|A|02319+8915|I| 1| 1| | | |  |   |       |     |     |    |S| |P|  8890|B+88    8 |          |          |0.68|F7:Ib-IIv SB|G\n'
    ----> 2 star = hipparcos.parse(line)
          3 print(star.ra.hours, star.dec.degrees)


    NameError: name 'hipparcos' is not defined


Constellation
-------------

Show a constellation using PyEphem, Skyfield, and Asterisms.

PyEphem
~~~~~~~


Skyfield
~~~~~~~~


Asterisms
~~~~~~~~~

and the equivalent using Asterisms

.. code:: python

    ori = a.Constellation(name='test')
    print(ori)
Precession
----------

The following example shows how to view a constellation a few thousand
years in the past, and a few thousand years in the future. It leverages
the `Vondrak <https://digitalvapor.github.io/vondrak/>`__ and Asterisms
projects to this end. If you want to see how to implement the equivalent
to this from scratch, please see the ``notebooks`` section of the
Asterisms project, or my blog at `DigitalVapor <http://antivapor.net>`__
where I've posted on it.

Create Constellation
~~~~~~~~~~~~~~~~~~~~

This creates a constellation using Asterisms.


Precess the Stars
~~~~~~~~~~~~~~~~~

The following precesses the stars of the constellation.

.. code:: python

    import vondrak as v
    print('using Vondrak version %s' % v.__version__)
Cartography
~~~~~~~~~~~

The following plots the constellation using basemap.


Helper Functions
----------------

Some of the helper functions that work in the background. These will
probably be moved over to the test section.

.. code:: python

    #==========
    # Midpoint
    #==========
    from skyfield.api import Star, earth, now
    import asterisms as a
    algol = Star(ra_hours=( 3,  8, 10.1315), dec_degrees=(40, 57, 20.332)) # approximately Algol
    mizar = Star(ra_hours=(13, 23, 55.5),    dec_degrees=(54, 55, 31)) # approximately Mizar
    algol_pos = earth(now()).observe(algol)
    mizar_pos = earth(now()).observe(mizar)
    # If given a tuple of (RA, Dec, Dist), return midpoint as (RA, Dec, Dist)
    p1 = algol_pos.radec()
    p2 = mizar_pos.radec()
    print(p1)
    print(p2)
    p3 = a.midpoint(p1, p2)
    print(p3)
    # If given a tuple of just (RA, Dec), return midpoint as (RA, Dec)
    p4 = (p1[0], p1[1])
    p5 = (p2[0], p2[1])
    print(p4)
    print(p5)
    p6 = a.midpoint(p4,p5)
    print(p6)

.. parsed-literal::

    (<Angle 03h 08m 10.13s>, <Angle +40deg 57' 20.3">, <Distance 2.06265e+14 AU>)
    (<Angle 13h 23m 55.50s>, <Angle +54deg 55' 31.0">, <Distance 2.06265e+14 AU>)
    (<Angle 08h 16m 02.82s>, <Angle +47deg 56' 25.7">, <Distance 2.06265e+14 AU>)
    (<Angle 03h 08m 10.13s>, <Angle +40deg 57' 20.3">)
    (<Angle 13h 23m 55.50s>, <Angle +54deg 55' 31.0">)
    (<Angle 08h 16m 02.82s>, <Angle +47deg 56' 25.7">)


