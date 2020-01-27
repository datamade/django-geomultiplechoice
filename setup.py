import setuptools

with open("README_pypi.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-geomultiplechoice",
    version="0.0.4",
    author="Bea Malsky",
    author_email="beamalsky@datamade.us",
    description="A Django widget to select multiple geographic areas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/datamade//django-geomultiplechoice",
    packages=setuptools.find_packages(include=['django_geomultiplechoice']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
