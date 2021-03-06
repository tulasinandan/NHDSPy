from setuptools import setup
import os
import sys

if sys.version_info < (3, 5):
    sys.exit('Python versions older than 3.5 are not supported.')

setup(name='nhdspy',
      version='0.0.1',
      description='Python wrapper for NHDS',
      author='David Stansby',
      author_email='dstansby@gmail.com',
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intended Audience :: Science/Research',
                   'Natural Language :: English',
                   'Programming Language :: Python :: 3',
                   'Topic :: Scientific/Engineering :: Physics'],
      install_requires=['numpy'],
      python_requires='>=3.5',
      packages=['NHDSPy'])
