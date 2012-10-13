# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages
from version import get_git_version

def read(filename):
    f = os.path.join(os.path.dirname(__file__), filename)
    if os.path.exists(f):
        return open(f).read()

setup(name='yle-dl',
    version = get_git_version(),
#    version='1.0a',
    description='librtmp plugin for Yle Areena',
    long_description=read('README'),
    author='Ville Korhonen',
    author_email='ville@xd.fi',
    url='https://github.com/ypcs/yle-dl',
    packages=find_packages('src'),
    package_dir={'': 'src',},
    license='GPLv2',
    install_requires=[
        'pycrypto',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        ],
    entry_points={
        'console_scripts': [
            'yle-dl = yledl.core:main',
        ],
    },
    )
