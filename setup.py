#!/usr/bin/env python

from distutils.core import setup
import versioneer

setup(name='wurstmineberg-common-python',
      cmdclass=versioneer.get_cmdclass(),
      version=versioneer.get_version(),
      description='Common functionality for Wurstmineberg python infrastructure',
      author='Wurstmineberg',
      author_email='mail@wurstmineberg.de',
      py_modules=["wmb", "_version"],
     )

