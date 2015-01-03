
Pierre Barbier made some amazing `Constellation
Maps <http://www.pbarbier.com/constellations/maps.html>`__ that inspired
me to create some astronomical depictions as if someone were viewing
from a telescope. The projection used is the `Azimuthal Equidistant
Projection <http://matplotlib.org/basemap/users/aeqd.html>`__. The
circle that circumscribes the stars is made using Eno Welzl's algorithm
for a smallest enclosing disk. The constellation's segments are from
H.A. Rey's asterisms. In many projections there is distortion, however
because the circle is centered using this algorithm, and this projection
is "equidistant", a circle that is centered is the only shape that won't
be distorted coincidently.

.. code:: python

    %pylab inline

.. parsed-literal::

    Populating the interactive namespace from numpy and matplotlib


.. code:: python

    import asterisms as a
    uma_segs = '67301 65378 65378 62956 62956 59774 59774 54061 54061 53910 53910 58001 58001 59774'
    uma = a.Constellation(name='Ursa Major',alt_name='Big Dipper',abbrev='UMA',segs=uma_segs)
    orion_segs = '26727 26311 26311 25930 28691 29426 29426 29038 29038 27913 27913 28691 29239 28614 28614 27989 27989 26727 26727 27366 24436 25281 25281 25930 25930 25336 25336 25813 25813 26207 25813 27989 25336 22449 22449 22549 22549 22797 22797 23123 22449 22509 22509 22845 22845 22833'
    ori = a.Constellation(name='Orion',alt_name='The Hunter',abbrev='ORI',segs=orion_segs)

.. parsed-literal::

    type is <class 'skyfield.starlib.Star'>
    make circle got type <class 'skyfield.starlib.Star'>
    yes! star
    type is <class 'skyfield.starlib.Star'>
    make circle got type <class 'skyfield.starlib.Star'>
    yes! star


.. code:: python

    from skyfield.units import Angle
    
    def greek(s):
        a = {'alf':u'α','bet':u'β','gam':u'γ','del':u'δ','eps':u'ε','zet':u'ζ','eta':u'η','the':u'θ','iot':u'ι','kap':u'κ','lam':u'λ','mu.':u'μ','nu.':u'ν','ksi':u'ξ','omi':u'ο','pi.':u'π','rho':u'ρ','sig':u'σ','tau':u'τ','ups':u'υ','phi':u'φ','chi':u'χ','psi':u'ψ','ome':u'ω'}
        n = u'⁰¹²³⁴⁵⁶⁷⁸⁹'
        try:
            letter = a[s[0:3]]
        except:
            return None
        try:
            letter = letter+n[int(s[3:5])]
        except:
            try:
                letter = letter+n[int(s[3])]+n[int(s[4])]
            except:
                pass
        return letter
    
    def cross_index(catalog, name):
        '''Uses the New Cross Index (`IV/27A <http://cdsarc.u-strasbg.fr/viz-bin/Cat?IV/27A>`_) to look up designations between catalogs. It also includes the visual magnitude, right ascension, magnitude and constellation abbreviation.
        
        Designations:
        
        Henry Draper Catalog Number ``HD`` (`III/135 <http://vizier.u-strasbg.fr/viz-bin/VizieR?-source=III/135>`_), 
        Durchmusterung Identification from HD Catalog ``DM`` (see `IV/27A note 1 <http://cdsarc.u-strasbg.fr/viz-bin/Cat?IV/27A#sRM3.1>`_), 
        General Catalogue of 33342 stars ``GC`` (`I/113 <http://vizier.u-strasbg.fr/viz-bin/VizieR?-source=I/113>`_), 
        Harvard Revised Number - BSC5 ``HR`` (`V/50 <http://vizier.u-strasbg.fr/viz-bin/VizieR?-source=V/50>`_), 
        Hipparcos Catalog ``HIP`` (`I/196 <http://vizier.u-strasbg.fr/viz-bin/VizieR?-source=I/196>`_)
        
        You can look solely for the Bayer ``Bayer`` *or* Flamsteed number ``Fl``, or return either with ``BFD``.
        
        `IV/27A note 2 <http://cdsarc.u-strasbg.fr/viz-bin/Cat?IV/27A#sRM3.2>`_ on HIP and CSI (`IV/9 <http://vizier.u-strasbg.fr/viz-bin/VizieR?-source=IV/9>`_) right ascensions and visual magnitude:
            
            Right ascensions, declinations and visual magnitudes for all stars were taken from the Hipparcos catalog and from the CSI for the stars that has no number in catalog Hipparcos.
            
        Here is an example of looking up a star in Orion's belt by using the Hipparcos number:
        
        ::
        
            sn_dict = cross_index('HIP','25930')
            print(sn_dict['Bayer'],sn_dict['Vmag'],sn_dict['Cst'])
        
        Excluding DE to Dec as a key abbreviation and the addition of epoch, the labels are the same as the New Cross Index.
        '''
        
        cross_index_url = 'ftp://cdsarc.u-strasbg.fr/pub/cats/IV/27A/catalog.dat'
        star_dict = {}
    
        try:
            data = open('catalog.dat','r')
        except:
            import wget
            wget.download(cross_index_url)
            data = open('catalog.dat','r')
            
        for l in data.readlines():
            s = {}
            s['HD'] = l[0:6]
            s['DM'] = l[7:19]
            s['GC'] = l[20:25]
            s['HR'] = l[26:30]
            if(s['HR'] == '    '): s['HR'] = None
            s['HIP'] = l[31:37]
            if(s['HIP'] == '      '): s['HIP'] = None
            ra = float(l[38:40])+float(l[40:42])/60.+float(l[42:47])/3600.
            s['RA'] = Angle(degrees=float(ra))
            if(l[48]=='+'): 
                sign=1
            else:
                sign=-1
            dec = sign*float(l[49:51])+float(l[51:53])/60.+float(l[53:57])/3600.
            s['Dec'] = Angle(degrees=float(dec))
            s['Vmag'] = l[58:63]
            s['Fl'] = l[64:67].strip()
            s['Bayer']= l[68:73]
            if(s['Bayer'] == '     '):
                s['Bayer'] = None
            else:
                try:
                    s['Bayer'] = greek(s['Bayer'])
                except:
                    pass
            if(s['Bayer']):
                s['BFD'] = s['Bayer']
            elif(s['Fl']):
                s['BFD'] = s['Fl']
            else:
                s['BFD'] = None
            s['Cst']  = l[74:77]
            s['epoch'] = 2000 # The New Cross Index (IV/27A) uses epoch 2000.
            if(s[catalog] is not None and s[catalog].lower().strip() == name.lower().strip()):
                return s
        return False
.. code:: python

    from mpl_toolkits.basemap import Basemap
    from matplotlib.font_manager import FontProperties
    import matplotlib.patches as patches
    import matplotlib.pyplot as plt
    import numpy as np
    from numpy import sin,arccos,arcsin,cos
    
    R_EARTH = 6370997.0 #default is arithmetic mean radius of the earth, force this value for sanity or if want to use a different value.
    
    def plot_line(ax, ob):
        x, y = ob.xy
        ax.plot(x, y, color=BLUE, linewidth=3, solid_capstyle='round', zorder=1)
        return
    
    def r2m(radians, radius=R_EARTH):
        '''Converts radians to meters using the arithmetic mean radius of the earth. 
        
        The default Basemap sphere radius is 6370997 meters. See `rsphere <http://matplotlib.org/basemap/api/basemap_api.html>`_
        
        This is *only* intended as a helper for the Basemap functions which take widths in meters.
        '''
        return radians*radius
    
    def sohcahtoa(x=None,y=None,r=None):
        '''A simple unit-circle functions used for the border circle text'''
        if(all([x,r])):
            return r*np.sin(np.arccos(x/r)) # or equivalently r*sqrt(1-((x*x)/(r*r)))
        elif(all([y,r])):
            return r*np.cos(np.arcsin(y/r)) # or equivalently r*sqrt(1-((y*y)/(r*r)))
        elif(all([x,y])):
            return np.hypot(x,y)
        else:
            raise ValueError('Need two of three parameters, x/y/r.')
            return None
    
    (cc_ra, cc_dec) = ori.circumcenter
    cc_x = cc_ra._degrees
    cc_y = cc_dec.degrees
    width=r2m(ori.circumcenter_radius.radians)*2
    #---------
    fig = plt.figure(figsize=(15,15))#,dpi=400)
    ax = fig.add_subplot(111,frameon=False)
    bm = Basemap(ax=ax, width=width, height=width, projection='aeqd', lat_0=cc_y, lon_0=cc_x, rsphere=R_EARTH)
    gca().invert_xaxis()
    #---------
    # http://www.linuxlibertine.org
    # http://sourceforge.net/projects/linuxlibertine
    prop = FontProperties(fname='_static/LinLibertine_Rah.ttf')
    #write my own roman converter maybe, so less dependencies
    from roman import toRoman
    # font_title = FontProperties()
    # font_title.set_family(['cursive','serif'])
    # font_title.set_size('large')
    # fig.suptitle(ori.name,fontsize=14,fontproperties=font_title)
    # ax.set_title(ori.alt_name,fontsize=12,fontproperties=font_title)
    # #---------
    # font_star = FontProperties()
    # font_star.set_family(['monospace'])
    # font_star.set_size('medium')
    #---------
    magscale = 2
    color = 'k'
    t_offx,t_offy = .04,.04
    #---------
    for star in ori.stars:
        star_ci = cross_index('HIP',repr(star.names['HIP']))
        if(star_ci):
            star.vmag = float(star_ci['Vmag'])
            star.alt_name = star_ci['BFD']
            star_ci.pop('RA'); star_ci.pop('Dec') # so not mixing catalog positions
        else:
            star.vmag = 5.5 # I suppose hide this
            star.alt_name = None
        #if(star_ci):
        #    star.names = star_ci
        r = (5.5 - star.vmag) * magscale # -1.44/13.4 Vmag range in CSI
        
        x,y = bm(star.ra._degrees, star.dec.degrees)
        tx,ty = bm(star.ra._degrees+t_offx*r, star.dec.degrees+t_offy*r)
        if(star.alt_name):
            #ax.text(tx,ty,star.alt_name,fontproperties=font_star,color=color)
            ax.text(tx,ty,star.alt_name,color=color,fontproperties=prop)
        else:
            print('note to self: check %s' % star.names['HIP'])
        bm.plot(x,y, marker='o', color=color, markersize=r, clip_on=False, linewidth=0.1)
    circle_x,circle_y = bm(cc_ra._degrees, cc_dec.degrees)
    #---------
    border0 = patches.Circle((circle_x,circle_y),radius=width*.5,facecolor='none',edgecolor='k',clip_on=False)
    border1 = patches.Circle((circle_x,circle_y),radius=width*.505,facecolor='none',edgecolor='k',clip_on=False)
    border2 = patches.Circle((circle_x,circle_y),radius=width*.527,facecolor='none',edgecolor='k',clip_on=False)
    ax.add_patch(border0)
    ax.add_patch(border1)
    ax.add_patch(border2)
    #---------
    def draw_grid(lat_maj=10,lat_min=5,lon_maj=10,lon_min=5,disp_maj=True,disp_min=False):
        '''set major grid with lat_maj, lon_maj.
        
        set minor grid with lat_min, lon_min.
        
        display major and minor grids with disp_maj, disp_min.'''
        
        lats = np.arange(-30,31,lat_min)
        lons = np.arange(70,111,lon_min)
        #lats = np.arange(-80,80,lat_min)
        #lons = np.arange(-180,181,lon_min)
        
        for lat in lats:
            x1,y1 = bm(lons[0],lat)
            x2,y2 = bm(lons[-1],lat)
            plt.plot([x1, x2], [y1, y2], 'k', lw=.5, clip_path=border0, linestyle=':')
            #for sign in [1,-1]:
            # for bottom half of circle, nudge a bit out
            # I believe this is from distortion and my hypothesis that this projection was immune to circular distortion was wrong
            #if((circle_y-y1)>0):
            #    text_r = width*.518
            #else:
            #    text_r = width*.515
            #text_x = sohcahtoa(y=circle_y-y1,r=text_r)
            # rely on the NaNs to tell us if we went outside the circle
            #if(not np.isnan(text_x)):
            #    rotation = sign*180*np.arcsin(text_x/text_r)/pi
            #    text(circle_x+sign*text_x,y1,lat,rotation=rotation,va='center',ha='center')
        for lon in lons:
            x1,y1 = bm(lon,lats[0])
            x2,y2 = bm(lon,lats[-1])
            plt.plot([x1, x2], [y1, y2], 'k', lw=.5, clip_path=border0, linestyle=':')
            for sign in [1,-1]:
                # for bottom half of circle, nudge a bit out
                # I believe this is from distortion and my hypothesis that this projection was immune to circular distortion was wrong
                if(sign<0):
                    text_r = width*.518
                else:
                    text_r = width*.515
                text_y = sohcahtoa(x=circle_x-x1,r=text_r)
                # rely on the NaNs to tell us if we went outside the circle
                if(not np.isnan(text_y)):
                    rotation = sign*180*np.arcsin((circle_x-x1)/text_r)/pi
                    text(x1,circle_y+sign*text_y,toRoman(lon),rotation=rotation,fontproperties=prop,va='center',ha='center')
                    
    draw_grid(disp_min=True)
    plt.show()
    #---------
    #savefig('clipping_example.png')

.. parsed-literal::

    note to self: check 29239


.. parsed-literal::

    -c:27: RuntimeWarning: invalid value encountered in arccos



.. image:: telescope_files/telescope_4_2.png


After initializing the constellation, visual magnitude and Bayer
designations are found by cross referencing the Hipparcos number with
the `HD-DM-GC-HR-HIP-Bayer-Flamsteed Cross
Index <http://cdsarc.u-strasbg.fr/viz-bin/Cat?IV/27A>`__. I contributed
a method to
`Python-Skyfield <https://github.com/brandon-rhodes/python-skyfield>`__
that parses this. **insert link**

http://www.ianridpath.com/startales/bayer.htm

and some
`Uranographie <http://lhldigital.lindahall.org/cdm/ref/collection/astro_images/id/1676>`__-like
numbering along the edges

Maybe name constellations like in
`Uranometria <http://lhldigital.lindahall.org/cdm/ref/collection/astro_atlas/id/118>`__

Convert to Roman numerals
`roman.py <http://docutils.sourceforge.net/docutils/utils/roman.py>`__

https://upload.wikimedia.org/wikipedia/commons/5/58/Mercator\_World\_Map.jpg
https://upload.wikimedia.org/wikipedia/commons/5/56/Nova\_et\_Accuratissima\_Terrarum\_Orbis\_Tabula\_%28J.Blaeu%2C\_1664%29.jpg

