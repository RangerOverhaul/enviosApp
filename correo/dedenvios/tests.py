from unittest import mock
from unittest.mock import patch

from django.test import TestCase, SimpleTestCase

# Create your tests here.


from .models import Package

'''
class TestingCase(TestCase):

    def test_sum_class_should_sum_arguments(self):
        self.assertEqual(Sumador_print(a=1, b=3), 1 + 3)

    @patch.object(Sum, 'calculate')
    def test_sum_function_should_use_sum_class(self, calculate_mocked):
        print('OUTPUT', type(calculate_mocked))
        calculate_mocked.return_value = 3
        self.assertEqual(Sumador_print(a=5, b=5), 3)
        self.assertEqual(1, calculate_mocked.call_count)


    def test_mock_somenthing(self):
        self.assertEqual(1, 1)
'''


class TestExitsUser(TestCase):
    package = 'datos/package/{pack_id}'

    def test_app_should_return_404_code_if_package_does_not_exists(self):
        reponse = self.client.post(path=self.package.format(pack_id=0))
        self.assertEqual(reponse.status_code, 404)

    def test_app_should_set_package(self):
        package = Package.objects.create(pack_id='1')
        try:
            self.assertFalse(package.objects.get(package.id).deleted)
            reponse = self.client.post(path=self.package.format(pack_id=package.id))
            self.assertEqual(reponse.status_code, 200)
            self.assertTrue(package.objects.get(package.id).deleted)
        finally:
            package.deleted()

