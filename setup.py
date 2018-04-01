from setuptools import setup

setup(
   name='reverso_api',
   version='1.0',
   description='A useful module',
   author='Ivan Tishchenko',
   author_email='johnny.tishchenko@gmail.com',
   packages=['reverso_api'],  #same as name
   install_requires=['numpy'], #external packages as dependencies
)