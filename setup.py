from setuptools import setup

setup(
    name='tempt',
    version='0.1',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'tempt=tempt:main',
        ],
    },
)
