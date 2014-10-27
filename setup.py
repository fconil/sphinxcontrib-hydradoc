# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('./README.md') as stream:
  long_desc = stream.read()

requires = ['Sphinx>=1.0.5']

setup(
    name='sphinxcontrib-hydradoc',
    version='0.1',
    url='http://packages.python.org/sphinxcontrib-hydradoc',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-hydradoc',
    license='LGPL',
    author='',
    author_email='',
    description='Support for including JSON-LD into Sphinx documents',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: LGPL',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
    test_suite= 'nose.collector'
)
