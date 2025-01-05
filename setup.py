from setuptools import setup, find_packages
import pathlib

# Read the contents of README.md for a nicer PyPI description
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="classical_ciphers",
    version="1.0.0",  # If you want automatic versioning from tags, consider using setuptools_scm
    packages=find_packages(),
    install_requires=[],
    setup_requires=["wheel"],  # Ensures wheel is installed before building
    python_requires=">=3.8",   # Matches your CI matrix (3.8, 3.9, 3.10)
    entry_points={
        "console_scripts": [
            "classical-ciphers=classical_ciphers.main:main",
        ],
    },
    author="Oussama Guelfaa",
    author_email="your_email@example.com",  # Optional but good practice
    description="A Python project for classical ciphers",
    long_description=README,                # Use your README as the package long description
    long_description_content_type="text/markdown",
    url="https://github.com/Oussama-Guelfaa/ClassicalCiphers",  # Adjust to your repo
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
