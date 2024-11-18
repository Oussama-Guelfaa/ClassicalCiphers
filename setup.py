from setuptools import setup, find_packages

setup(
    name='classical_ciphers',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'classical-ciphers=main:main',
        ],
    },
    author='Oussama Guelfaa',
    description='A Python project for classical ciphers',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)