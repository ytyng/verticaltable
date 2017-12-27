# -*- coding: utf-8 -*-

from __future__ import unicode_literals

menu = [
    ('cancel',
     ""),
    ('test',
     "./runtests.py"),
    ('flake8',
     "flake8 ."),
    ('upload to pypi',
     "./setup.py sdist; twine upload dist/*"),
]
