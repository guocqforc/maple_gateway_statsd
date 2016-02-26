# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="maple_gateway_statsd",
    version='0.1.1',
    zip_safe=False,
    platforms='any',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    install_requires=['statsd'],
    url="https://github.com/dantezhu/maple_gateway_statsd",
    license="MIT",
    author="dantezhu",
    author_email="zny2008@gmail.com",
    description="upload maple gateway stat to statsd",
)
