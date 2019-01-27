import os

from setuptools import setup, find_packages


ROOT = os.path.abspath(os.path.dirname(__file__))
NAME = '{{ cookiecutter.project_slug }}'

about = {}

with open(os.path.join(ROOT, 'README.md')) as f:
    readme = f.read()

with open(os.path.join(ROOT, NAME, '__about__.py')) as f:
    exec(f.read(), about)

with open(os.path.join(ROOT, 'requirements.txt')) as f:
    requires = f.readlines()

setup(name=about['__title__'],
      version=about['__version__'],
      description=about['__description__'],
      long_description=readme,
      long_description_content_type='text/markdown',
      author=about['__author__'],
      author_email=about['__author_email__'],
      packages=find_packages(exclude=('tests', 'docs')),
      install_requires=requires)
