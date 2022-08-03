from django.test import TestCase
from api.utils import Sum

# Create your tests here.


class UtilsTestCase(TestCase):

    def test_sum(self):
        params = {
            'val_1': 1,
            'val_2': 3,
        }
        result = Sum(params).call().get('result')
        self.assertEqual(result, 4)

