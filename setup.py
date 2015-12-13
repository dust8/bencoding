from setuptools import setup, find_packages


setup(
    name='bencoding',
    version='0.2.2',

    packages=find_packages('src'),
    package_dir={'': 'src'},

    zip_safe=True,

    description='bencoding is implemented over python3.',
    url='https://github.com/dust8/bencoding',

    keywords='bencode bencoding',
)
