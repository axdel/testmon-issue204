from django.test import TestCase as DjangoTestCase
from foo import tests as foo_methods


class BarTestCase(DjangoTestCase):

    
    def test_bar_1(self):
        foo_methods.bait()
        assert True
