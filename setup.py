from setuptools import setup, find_packages

setup(
    name='filery',
    version='0.25',
    description='File Path API for Python.',
    packages=[
        'filer',
        'filer.ffmpeg_wrapper',
        'filer.ffmpeg_wrapper.parsers',
              ]
,
    url='https://github.com/GabrielC101/filer',
    author='Gabriel Curio',
    author_email='',
    install_requires=[
        'marshmallow',
        'python-magic',
        'six',
        'xxhash'
    ],
    keywords=['system', 'linux'],
)
