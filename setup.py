import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='altvmasterlist',
    version='1.4',
    author="Nickwasused",
    author_email="nickwasused.social@protonmail.com",
    description="A package to use the alt:V Masterlist api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nickwasused/altv-python-masterlist",
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
         "Operating System :: OS Independent",
     ],
)