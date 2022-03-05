from django.test import TestCase

from django.test import SimpleTestCase
# SimpleTestCase is used because we are not using a database. 
# Create your tests here.

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        repsonse = self.client.get('/')

        # check whether home page exist
        self.assertEqual(repsonse.status_code, 200)

    def test_about_page_status_code(self):

        # check whether about page exist
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_contact_page_status_code(self):
        response = self.client.get('/contact/')

        # check whether about page exist
        self.assertEqual(response.status_code, 200)