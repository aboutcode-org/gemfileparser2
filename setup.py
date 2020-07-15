# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': "A library to parse Rubygem gemspec and Gemfile files and Cocoapods podspec and Podfile files using Python. Friendly fork of https://gitlab.com/balasankarc/gemfileparser",
    'author': 'nexB',
    'url': 'https://github.com/nexB/gemfileparser2',
    'download_url': 'https://github.com/nexB/gemfileparser2',
    'author_email': 'info@aboutcode.org',
    'version': '0.7.0',
    'license': 'GPL-3+ and MIT',
    'long_description': '''
Installation
~~~~~~~~~~~~

| If using pip, use the command ``sudo pip install gemfileparser2``
| Else use the following commands

::

    git clone https://github.com/balasankarc/gemfileparser2.git
    cd gemfileparser2
    python setup.py install

Usage
~~~~~

::

    from gemfileparser2 import GemfileParser
    parser = GemfileParser(<path to Gemfile>, <name of the application (optional)>)
    dependency_dictionary = parser.parse()

The parse() method returns a dict object of the following format

::

    {
    'development': [list of dependency objects inside group 'development'],
    'runtime': [list of runtime dependency objects],
    .
    .
    .}

Each dependency object contains the following attributes

::

    name - Name of the gem
    requirement - Version requirement
    autorequire - Autorequire value
    source - Source URL of the gem
    parent - Dependency of which gem
    group - Group in which gem is a member of (default : runtime)

Example
^^^^^^^

::

    from gemfileparser2 import GemfileParser
    n = GemfileParser('Gemfile', 'diaspora')
    deps = n.parse()
    for key in deps:
       if deps[key]:
           print key
           for dependency in deps[key]:
               print "\t", dependency

Copyright
~~~~~~~~~

2015-2018 Balasankar C balasankarc@autistici.org

License
~~~~~~~

gemfileparser is released under two licenses: `GNU GPL version 3 (or above) License` and `MIT License`_.

.. _GNU GPL version 3 (or above) License: http://www.gnu.org/licenses/gpl
''',
    'install_requires': ['nose'],
    'packages': ['gemfileparser2'],
    'scripts': [],
    'name': 'gemfileparser2'
}

setup(
    classifiers=[
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'License :: OSI Approved :: MIT',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ], **config)
