import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='altvmasterlist',  
    version='0.1',
    scripts=['altvmasterlist.py'] ,
    author="Nickwasused",
    author_email="nickwasused.social@protonmail.com",
    description="A package to use the alt:V Masterlist api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nickwasused/altv-python-masterlist",
    packages=setuptools.find_packages(),
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
)