from rest_framework.test import APITestCase
from django.urls import reverse
from api.models import Checkbox
# from collections import OrderedDict
from api.serializers import CheckboxSerializer


class CheckboxApiTestCase(APITestCase):

    def test_get(self):
        checkbox_1 = Checkbox.objects.create(name='checkbox_1')
        checkbox_2 = Checkbox.objects.create(name='checkbox_2')
        url = reverse('checkbox-list')
        response = self.client.get(url)
        # print(response.data)
        # data = OrderedDict([
        #     ('count', 2),
        #     ('next', None),
        #     ('previous', None),
        #     (
        #         'results',
        #         [
        #             OrderedDict([('id', 1), ('name', 'checkbox_1'), ('is_checked', False)]),
        #             OrderedDict([('id', 2), ('name', 'checkbox_2'), ('is_checked', False)]),
        #         ],
        #     ),
        # ])
        data = CheckboxSerializer([checkbox_1, checkbox_2], many=True).data
        self.assertEqual(response.data, data)

    def test_create(self):
        # checkbox_1 = Checkbox.objects.create(name='checkbox_1')
        # checkbox_2 = Checkbox.objects.create(name='checkbox_2')
        data = {
            'name': 'checkbox_1'
        }
        url = reverse('checkbox-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
