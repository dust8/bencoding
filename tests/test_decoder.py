from unittest import TestCase
from .context import bencoding
from bencoding import Decoder



class TestDecoder(TestCase):
    def test_decode(self):
        decoder = Decoder(b'i3e')
        self.assertEqual(3, decoder.decode())