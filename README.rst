Bencoding : BCODE for Python3
=============================

.. image:: https://img.shields.io/pypi/v/bencoding.svg
    :target: https://pypi.python.org/pypi/bencoding
    
Bencoding is a Bcode library for Python3.

.. code-block:: python

    >>> from bencoding import bdecode
    >>> with open('ubuntu-16.04.1-desktop-amd64.iso.torrent', 'rb') as f:
            data = bdecode(f.read())
    >>> data.keys()
    odict_keys([b'announce', b'announce-list', b'comment', b'creation date', b'info'])
    >>> data[b'info'][b'name'].decode()
    'ubuntu-16.04.1-desktop-amd64.iso'
    >>> data[b'info'][b'piece length']
    524288

Installation
------------

To install Bencoding, simply.

.. code-block:: bash

    $ pip install bencoding

Documentation
-------------

Documenttation is available at http://bencoding.readthedocs.io .
