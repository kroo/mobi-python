import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='mobi-python',
     version='0.0.1',
     scripts=[] ,
     author="Elliot Kroo",
     author_email="elliot@kroo.net",
     description="Mobi Python Library",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/kroo/mobi-python",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )