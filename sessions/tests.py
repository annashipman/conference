from django.test import TestCase
from sessions.views import get_title

class DefinedTitleTest(TestCase):
    def test_title_is_Anna(self):
        test_title = "Anna"
        actual_title = get_title(test_title)
        self.assertEqual(actual_title, "Anna")

    def test_title_is_not_Anna(self):
        test_title = "something else"
        actual_title = get_title(test_title)
        self.assertEqual(actual_title, "Shipman")
