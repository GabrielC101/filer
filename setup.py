from setuptools import setup, find_packages

setup(
    name='filer',
    version='0.24',
    packages=[
        'filer',
        'filer.ffmpeg_wrapper',
        'filer.ffmpeg_wrapper.parsers',
              ]
,
    url='',
    license='',
    author='Gabriel Curio',
    author_email='',
    description='',
    install_requires=[
        'marshmallow',
        'python-magic',
        'six',
        'xxhash'
    ]
)
