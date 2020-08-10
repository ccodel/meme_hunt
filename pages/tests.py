from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView
from meme_hunt.lib.time import TimeConverter
from meme_hunt.lib.test import standard_page_test

class HomePageTests(TestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)
        self.meme = Meme.objects.create(
            subtitle = 'dummy meme',
            start_date = TimeConverter.now(),
            end_date = TimeConverter.now(),
            secret_key = 12345
        )
        self.meme.save()

    def test_standard(self):
        standard_page_test(self, '/', 'home.html', HomePageView)

    # def test_homepage_latest_meme(self):
    #     now = TimeConverter.now()


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_standard(self):
        standard_page_test(self, '/about/', 'about.html', AboutPageView)
