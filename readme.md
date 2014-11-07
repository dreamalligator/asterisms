For eons[*](#eons), man has looked up at the night sky. What did they see before 1922?

**Goals:**

1. To divide the night sky into historical and cultural night skies.
2. To chart these night skies using the current boundary formats, and provide a database to start things off.

From [Wikipedia](https://en.wikipedia.org/wiki/Constellation#IAU_constellations):

> In [1922](http://articles.adsabs.harvard.edu/full/1922PA.....30..469R), [Henry Norris Russell](https://en.wikipedia.org/wiki/Henry_Norris_Russell) aided the IAU ([International Astronomical Union](https://en.wikipedia.org/wiki/International_Astronomical_Union)) in dividing the celestial sphere into 88 official [constellations](http://www.ianridpath.com/iaulist1.htm). Where possible, these modern constellations usually share the names of their Graeco-Roman predecessors, such as [Orion](https://en.wikipedia.org/wiki/Orion_%28constellation%29), Leo or Scorpius. The aim of this system is area-mapping, i.e. the division of the celestial sphere into [contiguous fields](http://www.iau.org/public/themes/constellations/). Out of the 88 modern constellations, 36 lie predominantly in the northern sky, and the other 52 predominantly in the southern.

> In 1930, the boundaries between the 88 constellations were devised by [Eugène Delporte](https://en.wikipedia.org/wiki/Eug%C3%A8ne_Joseph_Delporte) along vertical and horizontal lines of right ascension and declination. However, the data he used originated back to epoch B1875.0, which was when Benjamin A. Gould first made the proposal to designate boundaries for the celestial sphere, a suggestion upon which Delporte would base [his work](contribute). The consequence of this early date is that due to the precession of the equinoxes, the borders on a modern star map, such as epoch J2000, are already [somewhat skewed](http://cdsarc.u-strasbg.fr/ftp/cats/VI/49/constell.pdf) and no longer perfectly vertical or horizontal. This effect will increase over the years and centuries to come.

#Format
Will use the boundary coordinate format specified in the [IAU constellation](http://www.iau.org/public/themes/constellations/) page.

>  A text file containing a set of coordinates that defines the boundaries of the constellations in the sky. The format is: <br>
HH MM SS.SSSS| DD.DDDDDDD|XXX

> Where: <br>
> HH MM SS.SSSS defines the right ascension hour, minute and second with J2000 coordinates <br>
> DD.DDDDDDD defines the declination with J2000 coordinates <br>
> XXX is the abbreviation of the constellation name <br>
> | is the separator of the fields

> Example: <br>
> 22 57 51.6729| 35.1682358|AND

[Here](http://www.iau.org/static/public/constellations/txt/ori.txt) is Orion's boundary text file.

```
04 43 24.5665|  0.2375014|ORI
04 44 08.1669| 15.7364635|ORI
05 05 09.3423| 15.6755352|ORI
05 05 10.8669| 16.1754990|ORI
05 27 11.6910| 16.1101055|ORI
05 27 10.1358| 15.6101446|ORI
05 43 10.4751| 15.5619202|ORI
05 43 01.2137| 12.5621548|ORI
05 53 01.2887| 12.5318508|ORI
05 53 18.5201| 18.0314159|ORI
05 49 18.4757| 18.0435486|ORI
05 49 34.5105| 22.8764725|ORI
06 00 34.5690| 22.8430862|ORI
06 00 30.0373| 21.5098724|ORI
06 20 29.7906| 21.4491768|ORI
06 20 16.6981| 17.4495068|ORI
06 25 46.5402| 17.4328651|ORI
06 25 29.4633| 11.9332972|ORI
06 25 23.4397|  9.9334478|ORI
06 21 23.5275|  9.9455481|ORI
06 20 54.1633| -0.0537102|ORI
06 20 42.5141| -4.0534163|ORI
05 56 12.5693| -3.9790573|ORI
05 55 51.7897|-10.9785318|ORI
05 10 52.8075|-10.8432293|ORI
05 11 13.0549| -3.8437285|ORI
04 46 13.5261| -3.7708201|ORI
04 46 24.5553|  0.2289162|ORI
```

Or the format listed on [CDS Constellation Boundaries](http://vizier.cfa.harvard.edu/vizier/VizieR/constellations.htx) page. Also see [constellation boundary data](http://cdsarc.u-strasbg.fr/viz-bin/Cat?cat=VI%2F49) ([files](http://cdsarc.u-strasbg.fr/viz-bin/Cat?cat=VI%2F49&target=http&)) (1989) and [constbnd.txt](http://cdsarc.u-strasbg.fr/viz-bin/getCatFile_Redirect/?VI/49/constbnd.txt).

Orion as example again: [Constellation Page](http://vizier.cfa.harvard.edu/viz-bin/vizExec/Vgraph?VI/42&Ori) / [Postscript figure](http://vizier.cfa.harvard.edu/viz-bin/nph-Plot/Vgraph/ps?VI%2f42&Ori) / [Text](http://vizier.cfa.harvard.edu/viz-bin/nph-Plot/Vgraph/txt?VI%2f42&Ori)

```
#-- Constellation: Ori
#\*a(1875) [°]	\*d(1875) [°]
#Ori

069.2500   0.0000
069.2500  15.5000
074.5000  15.5000
074.5000  16.0000
080.0000  16.0000
080.0000  15.5000
084.0000  15.5000
084.0000  12.5000
086.5000  12.5000
086.5000  18.0000
085.5000  18.0000
085.5000  22.8333
088.2500  22.8333
088.2500  21.5000
093.2500  21.5000
093.2500  17.5000
094.6250  17.5000
094.6250  12.0000
094.6250  10.0000
093.6250  10.0000
093.6250   0.0000
093.6250  -4.0000
087.5000  -4.0000
087.5000 -11.0000
076.2500 -11.0000
076.2500  -4.0000
070.0000  -4.0000
070.0000   0.0000
069.2500   0.0000
```

The end goal will complete the night sky similar to the current designations for different night skies throughout history.

![sky](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Constellations_ecliptic_equirectangular_plot.svg/512px-Constellations_ecliptic_equirectangular_plot.svg.png 'Constellations ecliptic equirectangular plot')

[Detailed view here](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Constellations_ecliptic_equirectangular_plot.svg/1000px-Constellations_ecliptic_equirectangular_plot.svg.png).

#Eons
When I say eons, maybe I should tone it down to less than a million, but I'd like to think that the first hominids looked at the night sky in the early Miocene, 22 million years ago. If not, then at least by the end of the epoch 5 million years ago when apes were diversified enough to distinctly call some pre-human. It was recently found that [dung beetles watch the sky](http://www.sciencedirect.com/science/article/pii/S0960982212015072), so why not?

From [Wikipedia](https://en.wikipedia.org/wiki/Orion_%28constellation%29#History_and_mythology):

> The earliest depiction that has been linked to the constellation of Orion is a prehistoric ([Aurignacian](https://en.wikipedia.org/wiki/Aurignacian)) mammoth ivory carving found in a cave in the Ach valley in Germany in 1979. Archaeologists have estimated it to have been fashioned approximately [32,000 to 38,000 years ago](http://www.academia.edu/2548806/The_anthropoid_in_the_sky_Does_a_32_000_years_old_ivory_plate_show_the_constellation_Orion_combined_with_a_pregnancy_calendar).The distinctive pattern of Orion has been recognized in numerous cultures around the world, and many myths have been associated with it. It has also been used as a symbol in the modern world.

So, there's a lot to cover, but you've got to start somewhere, so let's start with some of these. Please add an [issue](https://github.com/digitalvapor/asterisms/issues) in the tracker for another specific culture, time, or possibly based on a specific work.

#Night Skies
Some night skies by culture:

* [Australian Aboriginal](https://en.wikipedia.org/wiki/Australian_Aboriginal_astronomy)
* Chakavian-Kaykavian
* [Chechen (Nakh)](https://en.wikipedia.org/wiki/Nakh_peoples#Cosmology_and_creation)
* [Chinese](https://en.wikipedia.org/wiki/Chinese_constellations)
* [Egyptian](https://en.wikipedia.org/wiki/Egyptian_astronomy)
* [Greco-Roman](https://en.wikipedia.org/wiki/Ancient_Greek_astronomy)
* [Hindu](https://en.wikipedia.org/wiki/Hindu_astrology) / [Indian](https://en.wikipedia.org/wiki/Indian_astronomy)
* Incan
* [Inuit](https://en.wikipedia.org/wiki/Inuit_astronomy)
* Korean
* [Maori]()
* [Medieval Islam](https://en.wikipedia.org/wiki/Astronomy_in_medieval_Islam)
* Mesopotamian ([Babylonian](https://en.wikipedia.org/wiki/Babylonian_star_catalogues)-Assyrian-Sumerian)
* Native American
* Nordic
* Sumerian
* [Tibetan](https://en.wikipedia.org/wiki/Tibetan_astronomy)

Some night sky works, by date:

* [Vedanga Jyotisha](https://en.wikipedia.org/wiki/Vedanga_Jyotisha) by Lagadha (1400-1200 BCE)
* [Poeticon astronomicon](https://en.wikipedia.org/wiki/Poeticon_astronomicon)  attributed to [Hyginus](https://en.wikipedia.org/wiki/Hyginus) (~1 CE)
* [Almagest](https://en.wikipedia.org/wiki/Almagest) by [Ptolemy](https://en.wikipedia.org/wiki/Ptolemy) (100-178 CE)
* [Book of Fixed Stars](https://en.wikipedia.org/wiki/Book_of_Fixed_Stars) by [al-Sufi](https://en.wikipedia.org/wiki/Abd_al-Rahman_al-Sufi) (964)
* [Cheonsang Yeolcha Bunyajido](https://en.wikipedia.org/wiki/Cheonsang_Yeolcha_Bunyajido) (1395)
* [hemispheres](http://www.ianridpath.com/startales/durer.htm) by [Dürer](https://en.wikipedia.org/wiki/Albrecht_D%C3%BCrer) (1515)
* Astronomiæ Instauratæ Progymnasmata by [Tycho Brahe](https://en.wikipedia.org/wiki/Tycho_Brahe) (1588)
* [Uranometria Omnium Asterismorum](https://en.wikipedia.org/wiki/Uranometria) by [Bayer](https://en.wikipedia.org/wiki/Johann_Bayer) (1603)
* [Rudolphine Tables](https://en.wikipedia.org/wiki/Rudolphine_Tables) by [Kepler](https://en.wikipedia.org/wiki/Johannes_Kepler) (1627)
* [Prodromus Astronomiae](https://en.wikipedia.org/wiki/Prodromus_Astronomiae) by [Johannes Hevelius](https://en.wikipedia.org/wiki/Johannes_Hevelius) (1690)

Also, see:

* [88 modern constellations in different languages](https://en.wikipedia.org/wiki/88_modern_constellations_in_different_languages).
* [former constellations](https://en.wikipedia.org/wiki/Former_constellations)

#Notebooks
For the moment, progress will be logged in the [notebooks](https://github.com/digitalvapor/asterisms/tree/master/notebooks) folder in the form of [IPython Notebooks](https://github.com/ipython/ipython).

To run, `ipython notebook`.

* [draw bounds](https://github.com/digitalvapor/asterisms/blob/master/notebooks/draw-bounds.ipynb) - Input IAU format constellation region points and output a constellation polygon. ![orion](notebooks/orion.png 'orion constellation')
* [mini-hipparcos](https://github.com/digitalvapor/asterisms/blob/master/notebooks/mini-hipparcos.ipynb) - Take a largish [Hipparcos](https://en.wikipedia.org/wiki/Hipparcos) database and minify it for use with the asterisms by [H. A. Rey](https://en.wikipedia.org/wiki/H._A._Rey). File reduced to 0.671% for 792 stars out of an original 117955. Also, discover we are missing [ksi UMa](https://en.wikipedia.org/wiki/Xi_Ursae_Majoris) in the [hip2.dat](https://pystaratlas.googlecode.com/files/hip2.dat) catalog.
* [proper motion](https://github.com/digitalvapor/asterisms/blob/master/notebooks/proper-motion.ipynb) - The change of α Ursa Major 100000 years from now. ![alphaUM](notebooks/alphaUM.png 'alpha ursa major')
* [stars](https://github.com/digitalvapor/asterisms/blob/master/notebooks/stars.ipynb) - An equirectangular plot of the stars, assign magnitude, and color spectrum. ![orion stars](notebooks/stars.png 'orion constellation')
* [curious asterisms](https://github.com/digitalvapor/asterisms/blob/master/notebooks/curious-asterisms.ipynb) - asterisms by [H. A. Rey](https://en.wikipedia.org/wiki/H._A._Rey), the creator of Curious George. Here is Gemeni holding hands. ![gemeni](notebooks/gemeni.png 'gemeni holding hands')

#Fork
Please feel free to contribute by forking, or make a [issue](https://github.com/digitalvapor/asterisms/issues). Be a coding historical [celestial cartographer](https://en.wikipedia.org/wiki/Celestial_cartography).

#License
This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
