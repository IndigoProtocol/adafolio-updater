from setuptools import setup, find_packages


with open("README.md", "r") as readme_file:
    readme = readme_file.read()


with open("requirements.txt", "r") as fh:
   requirements = fh.readlines()


setup(
    name="adafolio-updater",
    version="0.0.0",
    author="Indigo Labs",
    description="A simple CLI for managing adafolio lists",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[req for req in requirements if req[:2] != "# "],
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={
        'console_scripts': [
            'folio=adafolio.cli:folio',
        ],
    },
)
