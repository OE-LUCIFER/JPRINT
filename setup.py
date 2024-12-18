from setuptools import setup, find_packages
import os

def get_long_description():
    with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r', encoding='utf-8') as f:
        return f.read()


setup(
    name='jprinter',
    version='0.1.1',
    description='A Python library for enhanced printing and debugging.',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    author='Abhay Koul',
    author_email='helpingai5@gmail.com',
    url='https://github.com/OE-LUCIFER/JPRINT',  # Add the project's GitHub URL
    packages=find_packages(),
    install_requires=[
        'colorama',
        'executing',
        'pygments'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Debuggers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    keywords='debugging print logging development',  # Add keywords for better search visibility
    license='Apache 2.0', # add the correct licence
    project_urls={
        'Source': 'https://github.com/OE-LUCIFER/JPRINT',
        'Bug Reports': 'https://github.com/OE-LUCIFER/JPRINT/issues',
    },
    python_requires='>=3.7', # specify the minimum python version
)
