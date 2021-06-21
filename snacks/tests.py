from django import urls
from django.conf.urls import url
from django.http import response
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here

class snacks_test(SimpleTestCase):
    def test_home(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_html(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_about(self):
        url = reverse("about")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_html(self):
        url = reverse("about")
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'about.html')
        self.assertTemplateUsed(response, 'base.html')