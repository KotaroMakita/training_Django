from django.test import TestCase

# Create your tests here.

import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """was_published_recently() returns False for quesitons whose pub_date is in teh future."""
        time = timezone.now() + datetime.timedelta(days=30)
        future_quesiton = Question(pub_date=time)
        self.assertIs(future_quesiton.was_published_recently(),False)