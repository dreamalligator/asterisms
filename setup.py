import os
from setuptools import setup
from asterisms import __version__

def read(*filenames):
    return open(os.path.join(os.path.dirname(__file__),*filenames)).read()

setup(
    name = 'asterisms',
    version = __version__,
    description = 'Asterism and celestial cartography helper functions',
    long_description = read('readme.rst'),
    url = 'https://github.com/digitalvapor/asterisms',
    author = 'Tom Spalding',
    author_email = 'tommycs@mail.sfsu.edu',
    license = 'Creative Commons Attribution-ShareAlike 4.0 International License',
    keywords = ['astronomy', 'asterisms', 'constellations', 'cartography', 'history']
    packages = ['asterisms'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering :: Astronomy',
    ])
