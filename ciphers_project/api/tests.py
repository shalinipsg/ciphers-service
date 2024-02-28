from django.test import TestCase
from .ciphers import ciphers_fun
# Create your tests here.
class ciphersTest(TestCase):
    def test1(self):
        plain_text='hello'
        shift=1
        exp='ifmmp'
        self.assertEqual(exp,ciphers_fun(plain_text,shift))
class ciphersTest2(TestCase):
    def test1(self):
        plain_text='winter'
        shift=3
        exp='zlqwhu'
        self.assertEqual(exp,ciphers_fun(plain_text,shift))      