Quickstart
==========


Encode Data
-----------

For example:

.. code-block:: python

    >>> from bencoding import bencode
    >>> ping = {'t':'aa', 'y':'q', 'q':'ping', 'a':{'id':'abcdefghij0123456789'}}
    >>> ping_bencode = bencode(ping)
    >>> ping_bencode
    b'd1:ad2:id20:abcdefghij0123456789e1:q4:ping1:y1:q1:t2:aae'



Decode Data
-----------

For example:

.. code-block:: python

    >>> from bencoding import bdecode
    >>> ping_bdecode = bdecode(ping_bencode)
    >>> ping_bdecode
    OrderedDict([(b'a', OrderedDict([(b'id', b'abcdefghij0123456789')])), (b'q', b'ping'), (b'y', b'q'), (b't', b'aa')])


Your can use to parse torrent file.

.. code-block:: python

    with open('ubuntu-16.04.1-desktop-amd64.iso.torrent', 'rb') as f:
        data = bdecode(f.read())
        print(data[b'info'][b'name'].decode())
