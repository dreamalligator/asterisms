
The usage is to set projection to the values below. An example, after
initializing a constellation ``uma`` is to plot with
``uma.plot(projection='lambert')``.

**Basic Projection Covered** \*
`Aitoff <https://en.wikipedia.org/wiki/Aitoff_projection>`__ -
``aitoff`` \*
`Hammer <https://en.wikipedia.org/wiki/Hammer_projection>`__ -
``hammer`` \* `Lambert Azimuthal Equal-Area
Projection <https://en.wikipedia.org/wiki/Lambert_azimuthal_equal-area_projection>`__
- ``lambert`` \*
`Mollweide <https://en.wikipedia.org/wiki/Mollweide_projection>`__ -
``mollweide``

.. code:: python

    %pylab inline

.. parsed-literal::

    Populating the interactive namespace from numpy and matplotlib


.. code:: python

    import asterisms as a
    segs = '67301 65378 65378 62956 62956 59774 59774 54061 54061 53910 53910 58001 58001 59774'
    uma = a.Constellation(name='Ursa Major',name_alt='Big Dipper',abbrev='UMA',segs=segs)
    print(uma.circumcenter, uma.circumcenter_radius)

.. parsed-literal::

    '65378'
    '53910'
    '67301'
    '58001'
    '59774'
    '62956'
    '54061'
    type is <class 'skyfield.starlib.Star'>
    make circle got type <class 'skyfield.starlib.Star'>
    yes! star
    ((<Angle 12h 25m 38.05s>, <Angle +55deg 31' 55.7">), <Angle 21deg 24' 00.5">)


.. code:: python

    import matplotlib.pyplot as plt
    from asterisms.cartography import init_plot, plot, plot_circle
    
    f, ax1 = init_plot(figsize=(10,4))
    plot(uma.stars, ax1, color='blue', projection=None)
    plot([uma.circumcenter], ax1, color='red', projection=None)
    plot_circle(center=uma.circumcenter, radius=uma.circumcenter_radius, ax=ax1, lw=4, alpha=0.6, projection=None)



.. parsed-literal::

    <matplotlib.patches.Circle at 0x7f0f06620550>




.. image:: projections_files/projections_3_1.png


.. code:: python

    uma.plot(projection='lambert')


.. image:: projections_files/projections_4_0.png


.. code:: python

    import asterisms as a
    orion_segs = '26727 26311 26311 25930 28691 29426 29426 29038 29038 27913 27913 28691 29239 28614 28614 27989 27989 26727 26727 27366 24436 25281 25281 25930 25930 25336 25336 25813 25813 26207 25813 27989 25336 22449 22449 22549 22549 22797 22797 23123 22449 22509 22509 22845 22845 22833'
    ori = a.Constellation(name='Orion',name_alt='The Hunter',abbrev='ORI',segs=orion_segs)
    ori.plot()

.. parsed-literal::

    '22549'
    '25336'
    '22449'
    '22797'
    '27913'
    '22509'
    '23123'
    '25281'
    '29239'
    '26727'
    '22833'
    '27366'
    '26311'
    '29038'
    '29426'
    '24436'
    '28691'
    '27989'
    '26207'
    '22845'
    '25813'
    '25930'
    '28614'
    type is <class 'skyfield.starlib.Star'>
    make circle got type <class 'skyfield.starlib.Star'>
    yes! star


.. parsed-literal::

    /usr/lib/pymodules/python2.7/matplotlib/projections/geo.py:485: RuntimeWarning: invalid value encountered in arcsin
      theta = np.arcsin(y / np.sqrt(2))



.. image:: projections_files/projections_5_2.png


**Not Supported Yet** \*
https://en.wikipedia.org/wiki/Lambert\_conformal\_conic\_projection \*
https://en.wikipedia.org/wiki/Lambert\_cylindrical\_equal-area\_projection
\* `Stereographic
Projection <https://en.wikipedia.org/wiki/Stereographic_projection>`__

**Examples and Goals for me** \* Pierre Barbier's `Constellation
Maps <http://www.pbarbier.com/constellations/maps.html>`__ \* All-Sky
Plot: `Galactic plane in All Sky
Maps <https://leejjoon.github.io/matplotlib_astronomy_gallery/healpix/allsky_galactic_proj.html>`__
(CYP, CEA, CAR, MER, SFL, PAR, MOL), `CfA
Survey <https://leejjoon.github.io/matplotlib_astronomy_gallery/cfasurvey/cfasurvey.html>`__,
`WHAM <https://leejjoon.github.io/matplotlib_astronomy_gallery/allsky/allsky.html>`__
\* Pystaratlas' project `output
example <https://code.google.com/p/pystaratlas/downloads/detail?name=proj_output_example.pdf>`__
\* http://www.xubuntix.org/weblog/2009/01/python-astronomy-and-maps \*
https://www.astro.rug.nl/software/kapteyn/ \*
http://matplotlib.org/basemap/users/mapsetup.html \*
http://matplotlib.org/basemap/users/examples.html \*
http://matplotlib.org/basemap/api/basemap\_api.html \*
https://en.wikipedia.org/wiki/World\_Geodetic\_System \*
https://github.com/matplotlib/basemap/blob/master/examples/allskymap.py

.. code:: python

    from mpl_toolkits.basemap import Basemap
    
    width = 5000000
    bm = Basemap(width=width, height=width, projection='aeqd', lat_0=5.0, lon_0=80.0)
    bm.drawparallels(np.arange(-80,81,10), labels=[True,True,False,False])
    bm.drawmeridians(np.arange(-180,180,10), labels=[False,False,True,True])
    for star in ori.stars:
        x,y = bm(star.ra._degrees, star.dec.degrees)
        bm.plot(x,y, marker='o', color='r', markersize=10)
        


.. image:: projections_files/projections_7_0.png


.. code:: python

    # Visual Center
    from mpl_toolkits.basemap import Basemap
    width = 5000000
    (cc_ra, cc_dec) = ori.center
    cc_x = cc_ra._degrees
    cc_y = cc_dec.degrees
    bm = Basemap(width=width, height=width, projection='aeqd', lat_0=cc_y, lon_0=cc_x)
    bm.drawparallels(np.arange(-80,81,10), labels=[True,True,False,False])
    bm.drawmeridians(np.arange(-180,180,10), labels=[False,False,True,True])
    for star in ori.stars:
        x,y = bm(star.ra._degrees, star.dec.degrees)
        bm.plot(x,y, marker='o', color='r', markersize=10)
       


.. image:: projections_files/projections_8_0.png


.. code:: python

    # This example zooms to the circumcenter and converts the radius of the smallest enclosing disk to meters (because thats what Basemap wants, and doubles it for width).
    from mpl_toolkits.basemap import Basemap
    
    R_EARTH = 6370997.0 #default is arithmetic mean radius of the earth, force this value for sanity or if want to use a different value.
    TAU = 2*pi
    
    def r2m(radians, radius=R_EARTH):
        '''Converts radians to meters using the arithmetic mean radius of the earth. 
        
        The default Basemap sphere radius is 6370997 meters. See `rsphere <http://matplotlib.org/basemap/api/basemap_api.html>`_
        
        This is *only* intended as a helper for the Basemap functions which take widths in meters.
        '''
        return radians*radius
    
    #use the circumcenter to center
    (cc_ra, cc_dec) = ori.circumcenter
    cc_x = cc_ra._degrees
    cc_y = cc_dec.degrees
    width=r2m(ori.circumcenter_radius.radians)*2
    print(width)
    bm = Basemap(width=width, height=width, projection='aeqd', lat_0=cc_y, lon_0=cc_x, rsphere=R_EARTH)
    bm.drawparallels(np.arange(-80,81,10), labels=[True,True,False,False])
    bm.drawmeridians(np.arange(-180,180,10), labels=[False,False,True,True])
    for star in ori.stars:
        x,y = bm(star.ra._degrees, star.dec.degrees)
        bm.plot(x,y, marker='o', color='r', markersize=10)


.. parsed-literal::

    3389492.74537



.. image:: projections_files/projections_9_1.png


.. code:: python

    import matplotlib.patches as patches
    #use the circumcenter to center
    (cc_ra, cc_dec) = ori.circumcenter
    cc_x = cc_ra._degrees
    cc_y = cc_dec.degrees
    width=r2m(ori.circumcenter_radius.radians)*2
    
    fig = plt.figure()
    ax = fig.add_subplot(111,frameon=False)
    bm = Basemap(ax=ax, width=width, height=width, projection='aeqd', lat_0=cc_y, lon_0=cc_x, rsphere=R_EARTH)
    bm.drawparallels(np.arange(-80,81,10), labels=[True,True,False,False])
    bm.drawmeridians(np.arange(-180,180,10), labels=[False,False,True,True])
    for star in ori.stars:
        x,y = bm(star.ra._degrees, star.dec.degrees)
        bm.plot(x,y, marker='o', color='r', markersize=10,clip_on=False)
    circle_x,circle_y = bm(cc_ra._degrees, cc_dec.degrees)
    patch = patches.Circle((circle_x,circle_y),radius=width/2,facecolor='blue',clip_on=False)
    ax.add_patch(patch)



.. parsed-literal::

    <matplotlib.patches.Circle at 0x7f0f08e04490>




.. image:: projections_files/projections_10_1.png


.. code:: python

    (cc_ra, cc_dec) = ori.circumcenter
    cc_x = cc_ra._degrees
    cc_y = cc_dec.degrees
    width=r2m(ori.circumcenter_radius.radians)*2
    
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111,frameon=False)
    bm = Basemap(ax=ax, width=width, height=width, projection='aeqd', lat_0=cc_y, lon_0=cc_x, rsphere=R_EARTH)
    bm.drawparallels(np.arange(-80,81,10), labels=[True,True,False,False])
    bm.drawmeridians(np.arange(-180,180,10), labels=[False,False,True,True])
    for star in ori.stars:
        x,y = bm(star.ra._degrees, star.dec.degrees)
        bm.plot(x,y, marker='o', color='r', markersize=10,clip_on=False)
    circle_x,circle_y = bm(cc_ra._degrees, cc_dec.degrees)
    border0 = patches.Circle((circle_x,circle_y),radius=width/2,facecolor='none',edgecolor='k',clip_on=False)
    border1 = patches.Circle((circle_x,circle_y),radius=width*.51,facecolor='none',edgecolor='k',clip_on=False)
    ax.add_patch(border0)
    ax.add_patch(border1)



.. parsed-literal::

    <matplotlib.patches.Circle at 0x7f0f08e94990>




.. image:: projections_files/projections_11_1.png


I dont think clip paths get rid of grid lines(?) and I suppose I could
make a filled contour for the outside of the border, but I'd rather
leave it transparent. The immediate solution I see is to just make the
lines myself.

.. code:: python

    %pylab inline
    import asterisms as a
    orion_segs = '26727 26311 26311 25930 28691 29426 29426 29038 29038 27913 27913 28691 29239 28614 28614 27989 27989 26727 26727 27366 24436 25281 25281 25930 25930 25336 25336 25813 25813 26207 25813 27989 25336 22449 22449 22549 22549 22797 22797 23123 22449 22509 22509 22845 22845 22833'
    ori = a.Constellation(name='Orion',name_alt='The Hunter',abbrev='ORI',segs=orion_segs)

.. parsed-literal::

    Populating the interactive namespace from numpy and matplotlib
    '22549'
    '25336'
    '22449'
    '22797'
    '27913'
    '22509'
    '23123'
    '25281'
    '29239'
    '26727'
    '22833'
    '27366'
    '26311'
    '29038'
    '29426'
    '24436'
    '28691'
    '27989'
    '26207'
    '22845'
    '25813'
    '25930'
    '28614'
    type is <class 'skyfield.starlib.Star'>
    make circle got type <class 'skyfield.starlib.Star'>
    yes! star


.. code:: python

    from mpl_toolkits.basemap import Basemap
    import matplotlib.patches as patches
    
    R_EARTH = 6370997.0 #default is arithmetic mean radius of the earth, force this value for sanity or if want to use a different value.
    
    def r2m(radians, radius=R_EARTH):
        '''Converts radians to meters using the arithmetic mean radius of the earth. 
        
        The default Basemap sphere radius is 6370997 meters. See `rsphere <http://matplotlib.org/basemap/api/basemap_api.html>`_
        
        This is *only* intended as a helper for the Basemap functions which take widths in meters.
        '''
        return radians*radius
    
    (cc_ra, cc_dec) = ori.circumcenter
    cc_x = cc_ra._degrees
    cc_y = cc_dec.degrees
    width=r2m(ori.circumcenter_radius.radians)*2
    #---------
    fig = plt.figure(figsize=(8,8))
    title = '{0} - {1}'.format(ori.name,ori.name_alt)
    ax = fig.add_subplot(111,frameon=False,title=title)
    bm = Basemap(ax=ax, width=width, height=width, projection='aeqd', lat_0=cc_y, lon_0=cc_x, rsphere=R_EARTH)
    #---------
    for star in ori.stars:
        x,y = bm(star.ra._degrees, star.dec.degrees)
        bm.plot(x,y, marker='o', color='r', markersize=10, clip_on=False)
    circle_x,circle_y = bm(cc_ra._degrees, cc_dec.degrees)
    #---------
    border0 = patches.Circle((circle_x,circle_y),radius=width/2,facecolor='none',edgecolor='k',clip_on=False)
    border1 = patches.Circle((circle_x,circle_y),radius=width*.51,facecolor='none',edgecolor='k',clip_on=False)
    ax.add_patch(border0)
    ax.add_patch(border1)
    #---------
    # dashes = [100,.0001]
    # bm.drawparallels(np.arange(-80,81,5),clip_path=border0, linewidth=2, color='b', dashes=dashes)
    # bm.drawparallels(np.arange(-80,81,10), labels=[True,True,False,False],clip_path=border0, linewidth=5, dashes=dashes)
    # bm.drawmeridians(np.arange(-180,180,10), labels=[False,False,True,True],clip_path=border0,dashes=dashes)
    #---------
    # Will make a grid function here if need to
    def draw_grid(lat_maj=10,lat_min=5,lon_maj=10,lon_min=5,):
        x1,y1 = bm(80,20)
        x2,y2 = bm(80,-10)
        plt.plot([x1, x2], [y1, y2], 'green', lw=3,clip_path=border0)
    draw_grid()
    #---------
    #savefig('clipping_example.png')


.. image:: projections_files/projections_14_0.png


.. code:: python

    from mpl_toolkits.basemap import Basemap
    from matplotlib.font_manager import FontProperties
    import matplotlib.patches as patches
    # from matplotlib import rc
    # rc('text',usetex=True)
    
    R_EARTH = 6370997.0 #default is arithmetic mean radius of the earth, force this value for sanity or if want to use a different value.
    
    def r2m(radians, radius=R_EARTH):
        '''Converts radians to meters using the arithmetic mean radius of the earth. 
        
        The default Basemap sphere radius is 6370997 meters. See `rsphere <http://matplotlib.org/basemap/api/basemap_api.html>`_
        
        This is *only* intended as a helper for the Basemap functions which take widths in meters.
        '''
        return radians*radius
    
    (cc_ra, cc_dec) = ori.circumcenter
    cc_x = cc_ra._degrees
    cc_y = cc_dec.degrees
    width=r2m(ori.circumcenter_radius.radians)*2
    #---------
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111,frameon=False)
    bm = Basemap(ax=ax, width=width, height=width, projection='aeqd', lat_0=cc_y, lon_0=cc_x, rsphere=R_EARTH)
    #---------
    font_title = FontProperties()
    font_title.set_family(['cursive','serif'])
    font_title.set_size('large')
    fig.suptitle(ori.name,fontsize=14,fontproperties=font_title)
    ax.set_title(ori.name_alt,fontsize=12,fontproperties=font_title)
    #---------
    font_star = FontProperties()
    font_star.set_family(['monospace'])
    font_star.set_size('medium')
    #---------
    for star in ori.stars:
        x,y = bm(star.ra._degrees, star.dec.degrees)
        ax.text(x,y,star.names[0][1],fontproperties=font_star)
        #ax.text(x,y, r'$E=mc^2$', fontsize=15)# can use LaTeX for Bayer designations
        #ax.text(x,y,u'Άλφα') #or unicode
        color = '#111111'
        bm.plot(x,y, marker='o', color=color, markersize=5, clip_on=False, linewidth=0.1)
    circle_x,circle_y = bm(cc_ra._degrees, cc_dec.degrees)
    #---------
    border0 = patches.Circle((circle_x,circle_y),radius=width/2,facecolor='none',edgecolor='k',clip_on=False)
    border1 = patches.Circle((circle_x,circle_y),radius=width*.51,facecolor='none',edgecolor='k',clip_on=False)
    ax.add_patch(border0)
    ax.add_patch(border1)
    #---------
    def draw_grid(lat_maj=10,lat_min=5,lon_maj=10,lon_min=5,disp_maj=True,disp_min=False):
        '''set major grid with lat_maj, lon_maj.
        
        set minor grid with lat_min, lon_min.
        
        display major and minor grids with disp_maj, disp_min.'''
        
        #lats = np.arange(-80,81,lat_maj)
        #lons = np.arange(-180,180,lon_maj)
        
        lats = np.arange(-20,21,lat_min)
        lons = np.arange(70,101,lon_min)
        for lat in lats:
            x1,y1 = bm(lons[0],lat)
            x2,y2 = bm(lons[-1],lat)
            plt.plot([x1, x2], [y1, y2], 'k', lw=2, clip_path=border0)
        for lon in lons:
            x1,y1 = bm(lon,lats[0])
            x2,y2 = bm(lon,lats[-1])
            plt.plot([x1, x2], [y1, y2], 'k', lw=2, clip_path=border0)
        #plt.plot([x1, x2], [y1, y2], 'blue', lw=300)#,clip_path=border0)
      
    draw_grid(disp_min=True)
    #---------
    #savefig('clipping_example.png')


.. image:: projections_files/projections_15_0.png


