#!/usr/bin/env python

from setuptools import setup

setup(name='SR API',
      version='1.0',
      description='Tools for accessing the SR API (http://sverigesradio.se/sida/default.aspx?programid=2358)',
      author='Erik Forsberg',
      author_email='forsberg@efod.se',
      packages=['srapi', ],
      install_requires=['requests'],
      entry_points = {
        "console_scripts": [
            "srapi = srapi:tool",
            ],
        },

     )
