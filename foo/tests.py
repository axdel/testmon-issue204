from django.test import TestCase as DjangoTestCase


class FooTestCase(DjangoTestCase):

    def test_foo_1(self):
        assert True


def bait():
    pass