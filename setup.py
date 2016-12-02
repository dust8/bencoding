from setuptools import setup, find_packages
from bencoding import __version__ as version

setup(
    name='bencoding',
    version=version,
    description='bencoding is implemented over python3.',
    author="dust8",
    url='https://github.com/dust8/bencoding',
    packages=find_packages(exclude=['docs', 'tests*']),
    license='MIT',
    keywords='bcode bencode bencoding torrent bittorrent', )
