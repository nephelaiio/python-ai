from setuptools import setup

requirements = [
    'keras',
    'tensorflow',
    'anyconfig',
    'pandas',
    'h5py'
]

dev_requirements = [
    'tox',
    'pytest'
]

setup(name='nephelaiio.ai',
      version='0.1',
      description='Helper functions for AI operations',
      url='https://github.com/nephelaiio/python-ai',
      author='Ted Cook',
      author_email='teodoro.cook ((a)) gmail.com',
      license='MIT',
      packages=['nephelaiio.ai', 'nephelaiio.utils'],
      setup_requires=requirements,
      tests_require=dev_requirements)
