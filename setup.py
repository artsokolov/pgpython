import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='pgpython',  
     version='0.1',
     author="Sokolov Artem",
     author_email="sokolovartem6@gmail.com",
     description="Package that helps you to work with postgresql",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/c0nder/pgpython",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
