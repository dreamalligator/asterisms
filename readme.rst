.. image:: https://travis-ci.org/digitalvapor/asterisms.svg
    :target: https://travis-ci.org/digitalvapor/asterisms

.. image:: http://bottlepy.org/docs/dev/_static/Gittip.png
    :target: https://gratipay.com/digitalvapor

For `eons`_, man has looked up at the night sky. What did they see before 1922?

Goals
=====

1. To divide the night sky into historical and cultural night skies.
2. To chart these night skies using the current boundary formats, and provide a database and methodology to start things off.

From `Wikipedia <https://en.wikipedia.org/wiki/Constellation#IAU_constellations>`_:

    In `1922 <http://articles.adsabs.harvard.edu/full/1922PA.....30..469R>`_, `Henry Norris Russell <https://en.wikipedia.org/wiki/Henry_Norris_Russell>`_ aided the IAU (`International Astronomical Union <https://en.wikipedia.org/wiki/International_Astronomical_Union>`_) in dividing the celestial sphere into 88 official `constellations <http://www.ianridpath.com/iaulist1.htm>`_. Where possible, these modern constellations usually share the names of their Graeco-Roman predecessors, such as `Orion <https://en.wikipedia.org/wiki/Orion_%28constellation%29>`_, Leo or Scorpius. The aim of this system is area-mapping, i.e. the division of the celestial sphere into `contiguous fields <http://www.iau.org/public/themes/constellations/>`_. Out of the 88 modern constellations, 36 lie predominantly in the northern sky, and the other 52 predominantly in the southern.

    In 1930, the boundaries between the 88 constellations were devised by `Eugène Delporte <https://en.wikipedia.org/wiki/Eug%C3%A8ne_Joseph_Delporte>`_ along vertical and horizontal lines of right ascension and declination. However, the data he used originated back to epoch B1875.0, which was when Benjamin A. Gould first made the proposal to designate boundaries for the celestial sphere, a suggestion upon which Delporte would base his work. The consequence of this early date is that due to the precession of the equinoxes, the borders on a modern star map, such as epoch J2000, are already `somewhat skewed <http://cdsarc.u-strasbg.fr/ftp/cats/VI/49/constell.pdf>`_ and no longer perfectly vertical or horizontal. This effect will increase over the years and centuries to come.

Format
======

All bounds will use the boundary coordinate format specified in the `IAU constellation <http://www.iau.org/public/themes/constellations/>`_ page.

    | A text file containing a set of coordinates that defines the boundaries of the constellations in the sky. The format is:
    | HH MM SS.SSSS| DD.DDDDDDD|XXX

    | Where:
    | HH MM SS.SSSS defines the right ascension hour, minute and second with J2000 coordinates
    | DD.DDDDDDD defines the declination with J2000 coordinates
    | XXX is the abbreviation of the constellation name
    | | is the separator of the fields

    | Example:
    | 22 57 51.6729| 35.1682358|AND

`Here <http://www.iau.org/static/public/constellations/txt/ori.txt>`_ is Orion's boundary text file.

The end goal will complete the night sky similar to the current designations for different night skies throughout history. Here is an example of the current IAU bounds, see `below <#notebooks>`_ for more examples.

.. image:: notebooks/images/bounds_family.png
    :alt: iau constellation bounds by family'

The structure I am thinking all constellations and asterisms will use for this project is the following. Where the third field is the endonym of the asterism if applicable.

Example ``1952_rey_asterisms.dat``

``'gsq' 'great square' 'großen Platz' 4 113963 113881 113881 677 677 1067 1067 113963``

Or use the stellarium/pystaratlas styled text file structure.

Example ``1952_rey_constellationship.fab`` delimited by spaces:

``GSq 4 113963 113881 113881 677 677 1067 1067 113963``

Example ``1952_rey_constellation_names.fab`` delimited by tab characters:

``Gsq	"Great Square"	_("Great Square")``

When adding new asterisms and constellations, please provide an IPython Notebook. It should plot examples, as well as document the sources, and as much information as possible. In lieu of a notebook, please make an issue in the tracker about the subject. Any help or discussion is more than welcome.

Eons
====

When I say eons, maybe I should tone it down to less than a million, but I'd like to think that the first hominids looked at the night sky in the early Miocene, 22 million years ago. If not, then at least by the end of the epoch 5 million years ago when apes were diversified enough to distinctly call some pre-human. It was recently found that `dung beetles watch the sky <http://www.sciencedirect.com/science/article/pii/S0960982212015072>`_, so why not?

From `Wikipedia <https://en.wikipedia.org/wiki/Orion_%28constellation%29#History_and_mythology>`__:

    The earliest depiction that has been linked to the constellation of Orion is a prehistoric (`Aurignacian <https://en.wikipedia.org/wiki/Aurignacian>`_) mammoth ivory carving found in a cave in the Ach valley in Germany in 1979. Archaeologists have estimated it to have been fashioned approximately `32,000 to 38,000 years ago <http://www.academia.edu/2548806/The_anthropoid_in_the_sky_Does_a_32_000_years_old_ivory_plate_show_the_constellation_Orion_combined_with_a_pregnancy_calendar>`_.The distinctive pattern of Orion has been recognized in numerous cultures around the world, and many myths have been associated with it. It has also been used as a symbol in the modern world.

So, there's a lot to cover, but you've got to start somewhere, so let's start with some of these. Please add an `issue <https://github.com/digitalvapor/asterisms/issues>`_ in the tracker for another specific culture, time, or possibly based on a specific work.

Night Skies
===========

Some night skies by culture:

* `Australian Aboriginal <https://en.wikipedia.org/wiki/Australian_Aboriginal_astronomy>`_
* Chakavian-Kaykavian
* `Chechen (Nakh) <https://en.wikipedia.org/wiki/Nakh_peoples#Cosmology_and_creation>`_
* `Chinese <https://en.wikipedia.org/wiki/Chinese_constellations>`_
* `Egyptian <https://en.wikipedia.org/wiki/Egyptian_astronomy>`_
* `Greco-Roman <https://en.wikipedia.org/wiki/Ancient_Greek_astronomy>`_
* `Hindu <https://en.wikipedia.org/wiki/Hindu_astrology) / `Indian <https://en.wikipedia.org/wiki/Indian_astronomy>`_
* Incan
* `Inuit <https://en.wikipedia.org/wiki/Inuit_astronomy>`_
* Korean
* Maori
* `Medieval Islam <https://en.wikipedia.org/wiki/Astronomy_in_medieval_Islam>`_
* Mesopotamian (`Babylonian <https://en.wikipedia.org/wiki/Babylonian_star_catalogues)-Assyrian-Sumerian>`_
* Native American
* Nordic
* Sumerian
* `Tibetan <https://en.wikipedia.org/wiki/Tibetan_astronomy>`_

Some night sky works, by date:

* `Vedanga Jyotisha <https://en.wikipedia.org/wiki/Vedanga_Jyotisha>`_ by Lagadha (1400-1200 BCE)
* Iliad, Odyssey by Homer (~ 700 BC)
* Works and Days, Astronomy attributed to Hesiod (~700 BC)
* Eudoxus
* Aratus
* `Poeticon astronomicon <https://en.wikipedia.org/wiki/Poeticon_astronomicon>`_  attributed to `Hyginus <https://en.wikipedia.org/wiki/Hyginus>`_ (~1 CE)
* `Almagest <https://en.wikipedia.org/wiki/Almagest>`_ by `Ptolemy <https://en.wikipedia.org/wiki/Ptolemy>`_ (100-178 CE)
* `Dunhuang star chart <https://en.wikipedia.org/wiki/Dunhuang_Star_Chart>`_ 618–907 AD
* `Book of Fixed Stars <https://en.wikipedia.org/wiki/Book_of_Fixed_Stars>`_ by `al-Sufi <https://en.wikipedia.org/wiki/Abd_al-Rahman_al-Sufi>`_ (964)
* `Cheonsang Yeolcha Bunyajido <https://en.wikipedia.org/wiki/Cheonsang_Yeolcha_Bunyajido>`_ (1395)
* `hemispheres <http://www.ianridpath.com/startales/durer.htm>`_ by `Albrecht Dürer <https://en.wikipedia.org/wiki/Albrecht_D%C3%BCrer>`_ (1515)
* Astronomiæ Instauratæ Progymnasmata by `Tycho Brahe <https://en.wikipedia.org/wiki/Tycho_Brahe>`_ (1588)
* Petrus Plancius (~ 1600)
* Pieter Dirkszoon Keyser and Frederick de Houtman (~ 1600)
* `Uranometria Omnium Asterismorum <https://en.wikipedia.org/wiki/Uranometria>`_ by `Bayer <https://en.wikipedia.org/wiki/Johann_Bayer>`_ (1603)
* `Rudolphine Tables <https://en.wikipedia.org/wiki/Rudolphine_Tables>`_ by `Kepler <https://en.wikipedia.org/wiki/Johannes_Kepler>`_ (1627)
* `Prodromus Astronomiae <https://en.wikipedia.org/wiki/Prodromus_Astronomiae>`_ by `Johannes Hevelius <https://en.wikipedia.org/wiki/Johannes_Hevelius>`_ (1690)
* Nicolas Louis de Lacaille (1754)
* Uranographia by Johann Elert Bode (1801)

Also, see:

* `88 modern constellations in different languages <https://en.wikipedia.org/wiki/88_modern_constellations_in_different_languages>`_.
* `former constellations <https://en.wikipedia.org/wiki/Former_constellations>`_.
* Ian Ridpath's `Pictures in the sky: the origin and history of constellations <https://www.youtube.com/watch?v=nZm-QaKqS-Y>`_. See `t=1379 <https://www.youtube.com/watch?v=nZm-QaKqS-Y#t=1379>`_ for depiction of Transmission of the constellations from their origin up to the 16th century.

Notebooks
=========
For the moment, progress will be logged in the `notebooks <https://github.com/digitalvapor/asterisms/tree/master/notebooks>`_ folder in the form of `IPython Notebooks <https://github.com/ipython/ipython>`_. You can `view them with nbviewer <http://nbviewer.ipython.org/github/digitalvapor/asterisms/tree/master/notebooks/>`_.

To run, ``ipython notebook``.

Draw Bounds
-----------
`draw bounds <http://nbviewer.ipython.org/github/digitalvapor/asterisms/blob/master/notebooks/draw-bounds.ipynb>`_ - Input IAU format constellation region points and output a constellation polygon.

.. image:: notebooks/images/orion.png
    :alt: orion constellation

IAU Bounds
----------
`iau bounds <http://nbviewer.ipython.org/github/digitalvapor/asterisms/blob/master/notebooks/iau-bounds.ipynb>`_ -  A method to plot all IAU constellation bounds. The algorithms amend wrapping discontinuities and account for the poles. Also added functionality to group the constellations and color the polygons.

.. image:: notebooks/images/bounds_family.png
    :alt: iau constellation bounds by family

.. image:: notebooks/images/bounds_time.png
    :alt: iau constellation bounds by time

Mini-Hipparcos
--------------
`mini-hipparcos <http://nbviewer.ipython.org/github/digitalvapor/asterisms/blob/master/notebooks/mini-hipparcos.ipynb>`_ - Take a largish `Hipparcos <https://en.wikipedia.org/wiki/Hipparcos>`_ database and minify it for use with the asterisms by `H. A. Rey <https://en.wikipedia.org/wiki/H._A._Rey>`_. File reduced to 0.671% for 792 stars out of an original 117955. Also, discover we are missing `ksi UMa <https://en.wikipedia.org/wiki/Xi_Ursae_Majoris>`_ in the `hip2.dat <https://pystaratlas.googlecode.com/files/hip2.dat>`_ catalog.

Proper Motion
-------------
`proper motion <http://nbviewer.ipython.org/github/digitalvapor/asterisms/blob/master/notebooks/proper-motion.ipynb>`_ - The change of α Ursa Major 100000 years from now.

.. image:: notebooks/images/alphaUM.png
    :alt: alpha ursa major

Stars
-----
`stars <http://nbviewer.ipython.org/github/digitalvapor/asterisms/blob/master/notebooks/stars.ipynb>`_ - An equirectangular plot of the stars, assign magnitude, and color spectrum.

.. image:: notebooks/images/stars.png
    :alt: orion constellation

Curious Asterisms
-----------------
`curious asterisms <http://nbviewer.ipython.org/github/digitalvapor/asterisms/blob/master/notebooks/curious-asterisms.ipynb>`_ - asterisms by `H. A. Rey <https://en.wikipedia.org/wiki/H._A._Rey>`_, the creator of Curious George. Here is Gemeni holding hands.

.. image:: notebooks/images/gemeni.png
    :alt: gemeni holding hands

Far-flung Proper Motion
-----------------------
`far-flung-proper-motion <http://nbviewer.ipython.org/github/digitalvapor/asterisms/blob/master/notebooks/far-flung-proper-motion.ipynb>`_ - some discussion on long-term precession models.

Vondrak
-------
`vondrak <http://nbviewer.ipython.org/github/digitalvapor/asterisms/blob/master/notebooks/vondrak.ipynb>`_ - Translated Vondrák's precession model to Python. Create a precession matrix and implement it. Here is the precession of Polaris over 400000 years. I also released this `Vondrak code <https://github.com/digitalvapor/vondrak/>`_ as a standalone Python package. See the documentation at `https://digitalvapor.github.io/vondrak <https://digitalvapor.github.io/vondrak>`_.

.. image:: notebooks/images/polaris_long_term.png
    :alt: Long term precession of Polaris over 400000 years

Fork
====
Please feel free to contribute by forking, or make a `issue <https://github.com/digitalvapor/asterisms/issues>`_. Be a coding historical `celestial cartographer <https://en.wikipedia.org/wiki/Celestial_cartography>`_.

License
=======
This work is licensed under a `Creative Commons Attribution-ShareAlike 4.0 International License <http://creativecommons.org/licenses/by-sa/4.0/>`_.
