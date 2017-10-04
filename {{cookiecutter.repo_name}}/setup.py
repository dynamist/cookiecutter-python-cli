#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import {{cookiecutter.repo_name}}
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('README.md') as f:
    README = f.read()
with open('CHANGELOG.md') as f:
    HISTORY = f.read()

install_requires = [
    'docopt',
]
extras_require = [
    'haste-client',
]
tests_require = [
    'pytest',
    'tox',
]
download_url = '{}/tarball/v{}'.format(
    '{{cookiecutter.url}}',
    {{cookiecutter.repo_name}}.__version__
)

setup(
    name={{cookiecutter.repo_name}}.__name__,
    version={{cookiecutter.repo_name}}.__version__,
    description={{cookiecutter.repo_name}}.__doc__,
    long_description=README + "\n\n" + HISTORY,
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    url={{cookiecutter.repo_name}}.__url__,
    download_url=download_url,
    zip_safe=False,  # Prevent creation of egg
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'test': ["pytest"],
    },
    packages={
        '{{cookiecutter.repo_name}}',
    },
    entry_points={
        'console_scripts': [
            '{{cookiecutter.repo_name}} = {{cookiecutter.repo_name}}.cli:cli_entrypoint',
        ],
    },
    classifiers=[
        # 'Development Status :: 1 - Planning',
        'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
    ],
    platforms=["OS Independent"],
    license="Apache License 2.0"
)
