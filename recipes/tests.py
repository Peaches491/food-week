from django.test import TestCase

import datetime

from django.utils import timezone
from django.test import TestCase

from recipes.models import Recipe

class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Recipe(recipe_name="Test Recipe", add_time="time")
        self.assertEqual(future_question.was_added_recently(), False)
