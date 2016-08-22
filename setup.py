#!/usr/bin/env python

from setuptools import setup

setup(name='wurstmineberg-common-python',
      description='Common functionality for Wurstmineberg python infrastructure',
      author='Wurstmineberg',
      author_email='mail@wurstmineberg.de',
      py_modules=["wmb", "version", "_version"],
      use_scm_version = {
            "write_to": "_version.py",
          },
      setup_requires=["setuptools_scm"],
     )

