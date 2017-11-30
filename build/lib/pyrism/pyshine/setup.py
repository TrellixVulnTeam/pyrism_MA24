from setuptools import setup

setup(
    name='pyshine',
    version='0.0.1',
    description='Let there be light!',
    author='pyrismguy',
    author_email='pyrismguy@gmail.com',
    packages=['pyrism/pyshine'],
    install_requires=[
        'numpy',
        'cython'
    ]
)
