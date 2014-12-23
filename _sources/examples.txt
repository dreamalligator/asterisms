
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


Visual Center
-------------

This example shows how to calculate the visual center (unweighted) of a
list of stars with Asterisms. This could be useful if you wanted to
point a telescope, or a celestrial mapping program, to the center of a
constellation. I like to think of it as a visual barycenter.

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
    print(positions)
    a.center(positions)

.. parsed-literal::

    [(<Angle 03h 08m 10.13s>, <Angle +40deg 57' 20.3">, <Distance 2.06265e+14 AU>), (<Angle 13h 23m 55.50s>, <Angle +54deg 55' 31.0">, <Distance 2.06265e+14 AU>), (<Angle 18h 36m 56.34s>, <Angle +38deg 47' 01.3">, <Distance 2.06265e+14 AU>)]




.. parsed-literal::

    (<Angle 11h 43m 00.66s>, <Angle +44deg 53' 17.5">)



Hipparcos
---------

Skyfield has some built-in functions for working with the Hipparcos
catalogue. See
`hipparcos.py <https://github.com/brandon-rhodes/python-skyfield/blob/master/skyfield/data/hipparcos.py>`__.
My project currently relies on the Skyfield `pull request I
made <https://github.com/brandon-rhodes/python-skyfield/pull/36>`__. So,
I am going to leave this here as a note to self.

.. code:: python

    from skyfield.data import hipparcos
    line = 'H|       11767| |02 31 47.08|+89 15 50.9| 1.97|1|H|037.94614689|+89.26413805| |   7.56|   44.22|  -11.74|  0.39|  0.45|  0.48|  0.47|  0.55|-0.16| 0.05| 0.27|-0.01| 0.08| 0.05| 0.04|-0.12|-0.09|-0.36|  1| 1.22| 11767| 2.756|0.003| 2.067|0.003| | 0.636|0.003|T|0.70|0.00|L| | 2.1077|0.0021|0.014|102| | 2.09| 2.13|   3.97|P|1|A|02319+8915|I| 1| 1| | | |  |   |       |     |     |    |S| |P|  8890|B+88    8 |          |          |0.68|F7:Ib-IIv SB|G\n'
    star = hipparcos.parse(line)
    print(star.ra.hours, star.dec.degrees)

.. parsed-literal::

    (2.5303010234979411, 89.264109507429168)


.. code:: python

    import gzip
    from skyfield.data import hipparcos
    from skyfield.data import cache as default_cache
    url = 'ftp://cdsarc.u-strasbg.fr/cats/I/239/hip_main.dat.gz'
    
    def load2(is_match, cache=default_cache):
        with cache.open_url(url, days_old=9999) as f:
            data = gzip.GzipFile(fileobj=f)
            #data = gzip.open('hip_main.dat.gz')
            for line in data.readlines():
                id = line[8:14]
                if is_match(id):
                   yield hipparcos.parse(line)
                    
    which = '11767'
    is_match = which.rjust(6).encode('ascii').__eq__
    for star in load2(is_match):
        s = star
        print(s)
        
    print((s.ra, s.dec))

.. parsed-literal::

    Star(ra_hours=2.5303010234979411, dec_degrees=89.264109507429168, ra_mas_per_year=44.22, dec_mas_per_year=-11.74, parallax_mas=7.56, names=[('HIP', 11767)])
    (<Angle 02h 31m 49.08s>, <Angle 89deg 15' 50.8">)


.. code:: python

    from skyfield.data import hipparcos
    hipparcos.get('11767')

.. parsed-literal::

    '11767'




.. parsed-literal::

    Star(ra_hours=2.5303010234979411, dec_degrees=89.264109507429168, ra_mas_per_year=44.22, dec_mas_per_year=-11.74, parallax_mas=7.56, names=[('HIP', 11767)])



Initialize a Constellation
--------------------------

You can initialize a constellation with the following code. The bare
minimum needed is really just a name and a list of star segments. At the
time of writing, all of the constellations are (to oversimplify the
format) just lists of star segments. Each star is listed by the
Hipparcos number. The only reason I chose this nomenclature is because
others were already using HIP numbers in their constellationship.fab
files.

.. code:: python

    import asterisms as a
    segs = '67301 65378 65378 62956 62956 59774 59774 54061 54061 53910 53910 58001 58001 59774'
    uma = a.Constellation(name='Ursa Major',name_alt='Big Dipper',abbrev='UMA',segs=segs)

.. parsed-literal::

    '65378'
    '53910'
    '67301'
    '58001'
    '59774'
    '62956'
    '54061'


Constellation Properties
~~~~~~~~~~~~~~~~~~~~~~~~

Each constellation instance has some basic properties, such as ``name``,
``name_alt``, abbreviation ``abbrev``, number of segments ``segs_n``,
and segments ``segs``. Segments is a list of an even number of star
segments, named by Hipparcos number.

.. code:: python

    print(uma.name)
    print(uma.name_alt)
    print(uma.abbrev)
    print(uma.segs)
    print(uma.segs_n)

.. parsed-literal::

    Ursa Major
    Big Dipper
    UMA
    ['67301', '65378', '65378', '62956', '62956', '59774', '59774', '54061', '54061', '53910', '53910', '58001', '58001', '59774']
    7


When given the list of Hipparcos numbered segments, the Constellation
inititializes a list of stars by using Skyfield's
`hipparcos.get <https://github.com/brandon-rhodes/python-skyfield/blob/master/skyfield/data/hipparcos.py>`__
method. It also passes these stars along and calculates the visual
(unweighted) center of the constellation. By this, it is meant that it
is the mean position. This is a tuple of right ascension and declination
in Skyfield's Angle type.

.. code:: python

    print(uma.stars)
    print(uma.center)

.. parsed-literal::

    [Star(ra_hours=13.398761920264775, dec_degrees=54.925361752393151, ra_mas_per_year=121.23, dec_mas_per_year=-22.01, parallax_mas=41.73, names=[('HIP', 65378)]), Star(ra_hours=11.030687999605183, dec_degrees=56.382426786427374, ra_mas_per_year=81.66, dec_mas_per_year=33.74, parallax_mas=41.07, names=[('HIP', 53910)]), Star(ra_hours=13.792343787984251, dec_degrees=49.313265059674272, ra_mas_per_year=-121.23, dec_mas_per_year=-15.56, parallax_mas=32.39, names=[('HIP', 67301)]), Star(ra_hours=11.897179848125406, dec_degrees=53.694760084185191, ra_mas_per_year=107.76, dec_mas_per_year=11.16, parallax_mas=38.99, names=[('HIP', 58001)]), Star(ra_hours=12.257100034120432, dec_degrees=57.032616901786447, ra_mas_per_year=103.56, dec_mas_per_year=7.81, parallax_mas=40.05, names=[('HIP', 59774)]), Star(ra_hours=12.900485951888628, dec_degrees=55.959821158352696, ra_mas_per_year=111.74, dec_mas_per_year=-8.99, parallax_mas=40.3, names=[('HIP', 62956)]), Star(ra_hours=11.062130192490219, dec_degrees=61.75103320112995, ra_mas_per_year=-136.46, dec_mas_per_year=-35.25, parallax_mas=26.38, names=[('HIP', 54061)])]
    (<Angle 12h 20m 02.75s>, <Angle +55deg 34' 47.6">)


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

.. parsed-literal::

    using Vondrak version 0.03


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
    from asterisms.geometry import midpoint
    algol = Star(ra_hours=( 3,  8, 10.1315), dec_degrees=(40, 57, 20.332)) # approximately Algol
    mizar = Star(ra_hours=(13, 23, 55.5),    dec_degrees=(54, 55, 31)) # approximately Mizar
    algol_pos = earth(now()).observe(algol)
    mizar_pos = earth(now()).observe(mizar)
    # If given a tuple of (RA, Dec, Dist), return midpoint as (RA, Dec, Dist)
    p1 = algol_pos.radec()
    p2 = mizar_pos.radec()
    print(p1)
    print(p2)
    p3 = midpoint(p1, p2)
    print(p3)
    # If given a tuple of just (RA, Dec), return midpoint as (RA, Dec)
    p4 = (p1[0], p1[1])
    p5 = (p2[0], p2[1])
    print(p4)
    print(p5)
    p6 = midpoint(p4,p5)
    print(p6)

.. parsed-literal::

    (<Angle 03h 08m 10.13s>, <Angle +40deg 57' 20.3">, <Distance 2.06265e+14 AU>)
    (<Angle 13h 23m 55.50s>, <Angle +54deg 55' 31.0">, <Distance 2.06265e+14 AU>)
    (<Angle 08h 16m 02.82s>, <Angle +47deg 56' 25.7">, <Distance 2.06265e+14 AU>)
    (<Angle 03h 08m 10.13s>, <Angle +40deg 57' 20.3">)
    (<Angle 13h 23m 55.50s>, <Angle +54deg 55' 31.0">)
    (<Angle 08h 16m 02.82s>, <Angle +47deg 56' 25.7">)


