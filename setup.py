import setuptools

with open("README_pypi.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-geomultiplechoice",
    version="0.0.5",
    author="Bea Malsky",
    author_email="beamalsky@datamade.us",
    description="A Django widget to select multiple geographic areas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/datamade//django-geomultiplechoice",
    packages=['django_geomultiplechoice'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
