from django.test import TestCase as DjangoTestCase
from foo.tests import *


class BarTestCase(DjangoTestCase):

    def setUp(self):
        self.foo_tests = FooTestCase()

    def test_bar_1(self):
        self.foo_tests = FooTestCase()
        self.foo_tests.test_foo_1()
        assert True

    def test_bar_2(self):
        assert True

    def test_bar_3(self):
        assert True

    def test_bar_4(self):
        assert True