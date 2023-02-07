from django.test import TestCase as DjangoTestCase
from bar.tests import BarTestCase


class Bar2TestCase(DjangoTestCase):

    def setUp(self):
        self.bar_tests = BarTestCase()

    def test_bar2_1(self):
        self.bar_tests = BarTestCase()
        self.bar_tests.test_bar_1()
        assert True

    def test_bar2_2(self):
        assert True

    def test_bar2_3(self):
        assert True

    def test_bar2_4(self):
        assert True