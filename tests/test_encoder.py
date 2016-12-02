from unittest import TestCase

from .context import bencoding
from bencoding import Encoder


class TestEncoder(TestCase):
    def test_encode(self):
        encoder = Encoder(3)
        self.assertEqual(b'i3e', encoder.encode())
