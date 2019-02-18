from django.test import TestCase

from .models import ShortUrl, User

# Create your tests hereself.


class ShortUrlViewTests(TestCase):
    def test_short_url_display(self):
        surl1 = ShortUrl(short_url="ABC123",
                        full_url="http://www.example.com",
                        submitter=User())
        response = self.client.get('/!{}'.format(surl1.short_url))
        self.assertContains(response, surl1.full_url)
