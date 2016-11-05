# from django.test import TestCase
from selenium import webdriver

# Create your tests here.
browser = webdriver.Chrome()
browser.get('http://localhost:8000')

assert 'Django' in browser.title