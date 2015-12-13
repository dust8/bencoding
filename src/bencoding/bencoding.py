'''
bencoding is implemented over python3.
'''


class BencodingError(Exception):
    pass


def bencode(x):
    '''
    >>> bencode('spam')
    b'4:spam'

    >>> bencode(3)
    b'i3e'

    >>> bencode(['spam', 'eggs'])
    b'l4:spam4:eggse'

    >>> bencode({'cow': 'moo', 'spam': 'eggs'})
    b'd3:cow3:moo4:spam4:eggse'

    >>> bencode({'spam': ['a', 'b']})
    b'd4:spaml1:a1:bee'
    '''
    if isinstance(x, str):
        try:
            data = x.encode('latin1')
        except:
            data = x.encode()
        return str(len(data)).encode('latin1')+b':'+data
    elif isinstance(x, bytes):
        return str(len(x)).encode('latin1')+b':'+x
    elif isinstance(x, (int, float)):
        return b'i'+str(x).encode('latin1')+b'e'
    elif isinstance(x, list):
        data = b''.join([bencode(i) for i in x])
        return b'l'+data+b'e'
    elif isinstance(x, dict):
        items = sorted(list(x.items()))
        data = b''.join([bencode(k) + bencode(v) for k, v in items])
        return b'd'+data+b'e'
    else:
        raise BencodingError('bencode error')


def bdecode(x):
    '''
    >>> bdecode(b'4:spam')
    'spam'

    >>> bdecode(b'i3e')
    3

    >>> bdecode(b'l4:spam4:eggse')
    ['spam', 'eggs']

    >>> d = {'cow': 'moo', 'spam': 'eggs'}
    >>> d == bdecode(b'd3:cow3:moo4:spam4:eggse')
    True
    '''
    try:
        r, f = _bdecode(x)
    except:
        raise BencodingError('bdecode error')
    return r


def _bdecode(x, f=0):
    r = x[f]
    int_list = [ord(str(i)) for i in range(10)]

    if r in int_list:
        colon = x.index(b':', f)
        n = int(x[f:colon])
        colon += 1
        try:
            return x[colon:colon+n].decode(), colon+n
        except:
            return x[colon:colon+n], colon+n
    elif r == ord(b'i'):
        f += 1
        newf = x.index(b'e', f)
        n = int(x[f:newf])
        return n, newf+1
    elif r == ord(b'l'):
        r, f = [], f+1
        while x[f] != ord(b'e'):
            v, f = _bdecode(x, f)
            r.append(v)
        return r, f+1
    elif r == ord(b'd'):
        r, f = {}, f+1
        while x[f] != ord(b'e'):
            k, f = _bdecode(x, f)
            r[k], f = _bdecode(x, f)
        return r, f+1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
