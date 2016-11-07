from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

class HomePage(TestCase):

    def test_home_page_can_remmeber_post_requests(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new item'
        response = home_page(request)

        self.assertIn('A new item', response.content.decode())
