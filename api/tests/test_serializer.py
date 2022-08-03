from django.test import TestCase
from api.models import Checkbox
from api.serializers import CheckboxSerializer


class SerializerTestCase(TestCase):

    def test_serialize(self):
        checkbox_1 = Checkbox.objects.create(name='checkbox_1')
        checkbox_2 = Checkbox.objects.create(name='checkbox_2')
        ser_data = CheckboxSerializer([checkbox_1, checkbox_2], many=True).data
        exp_data = [
            {
                'id': 1,
                'name': 'checkbox_1',
                'is_checked': False,
            },
            {
                'id': 2,
                'name': 'checkbox_2',
                'is_checked': False,
            },
        ]
        self.assertEqual(exp_data, ser_data)
