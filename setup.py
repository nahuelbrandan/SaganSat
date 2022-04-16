"""Setup of the project."""

import os

from setuptools import (
    setup,
    find_packages,
)

from saganSat import settings

SCRIPT = ['main.py']

with open("requirements.txt") as f:
    required = f.read().splitlines()

here = os.path.dirname(os.path.realpath(__file__))

setup(
    name='saganSat',
    version=settings.VERSION,
    url=settings.CONTACT['url'],
    license=settings.LICENCE['name'],
    author=settings.CONTACT['author'],
    keywords="simulate tasking satellite fleet",
    install_requires=required,
    author_email=settings.CONTACT['email'],
    description=settings.DESCRIPTION,
    long_description=settings.LONG_DESCRIPTION,
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    entry_points={
        'console_scripts': ['saganSat=main:main']
    },
    test_suite="tests",
    platforms="any",
    classifiers=[
        "Development Status :: 1 - Development",
        "Programming Language :: Python :: >3.6",
        "Environment :: Console",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    scripts=SCRIPT,
)
