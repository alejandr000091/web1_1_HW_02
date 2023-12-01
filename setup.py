#work1
from setuptools import setup, find_namespace_packages

setup(name = "bhb",
      version="0.11.4",
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['bhb = hw_1_01.hw_1_01:main']})