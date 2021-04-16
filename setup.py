# small testing project done during exchange semester at Temple University

from setuptools import setup

setup(
    name='deepnet',
    version='1.0.0',
    packages=['deepnet'],
    url='',
    license='',
    author='João Pedro Peters Barbosa',
    author_email='tul43753@temple.edu',
    description='',
    install_requires=['torch', 'torch-vision'],
    package_data = {'data': ['*.txt']}
)
