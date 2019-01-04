import os

from setuptools import setup

ROOT = os.path.abspath(os.path.dirname(__file__))
NAME = '{{ cookiecutter.project_slug }}'

about = {}

with open(os.path.join(ROOT, 'README.md')) as f:
    readme = f.read()

with open(os.path.join(ROOT, NAME, '__about__.py')) as f:
    exec(f.read(), about)

setup(name=about['__name__'],
      version=about['__version__'],
      description=about['__description__'],
      long_description=readme,
      long_description_content_type='text/markdown',
      author=about['__author__'],
      author_email=about['__author_email__'],
      packages=['{{ cookiecutter.project_slug }}'])
