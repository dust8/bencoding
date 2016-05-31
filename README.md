# Introducing bencoding

bencoding is implemented over python3.

## Installation

```
pip install bencoding
```

## Usage

```
>>> from bencoding import bencode, bdecode
>>> ping = {"t":"aa", "y":"q", "q":"ping", "a":{"id":"abcdefghij0123456789"}}
>>> bencoded = bencode(ping)   
>>> bencoded
b'd1:ad2:id20:abcdefghij0123456789e1:q4:ping1:t2:aa1:y1:qe'    
>>> ping2 = bdecode(bencoded)
>>> ping2
{'t': 'aa', 'y': 'q', 'a': {'id': 'abcdefghij0123456789'}, 'q': 'ping'}
>>> bencoded == bencode(ping2)
True
```
