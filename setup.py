from setuptools import setup, find_packages

setup(
    name='jprint',
    version='0.1.0',
    description='A Python library for enhanced printing and debugging.',
    long_description='jprint is a Python library that provides enhanced printing capabilities, aiming to be a versatile replacement for the standard `print` function. It incorporates features from `print`, `pprint`, and `rich.print` to offer more control over output formatting and debugging.',
    author='Abhay Koul',
    author_email='abhaykoul123@gmail.com',
    packages=find_packages(),
    install_requires=[
        'colorama',
        'executing',
        'pygments'
    ],
)
