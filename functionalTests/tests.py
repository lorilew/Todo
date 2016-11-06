import unittest
from unittest import skip

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_starting_a_new_todo_list(self):
        # Nancy has heard about a cool new to-do lists app,
        # she goes to it's homepage.
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-do', self.browser.title)
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-do', header.text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new-item')
        self.assertEqual('Enter to-do item here.', inputbox.get_attribute('placeholder'))

        # She types 'Buy peacock feathers' into a text box.
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # '1: Buy peacock feathers' as an Item on the to-do list
        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn(
            '1: Buy peacock feathers',
            [row.text for row in rows]
        )

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly'
        inputbox = self.browser.find_element_by_id('id_new-item')
        self.assertEqual('Enter to-do item here.', inputbox.get_attribute('placeholder'))

        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items in her list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn(
            '1: Buy peacock feathers',
            [row.text for row in rows]
        )
        self.assertIn(
            '2: Use peacock feathers to make a fly',
            [row.text for row in rows]
        )
        # Nancy wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect
        self.fail("Finish the test")

        # She visits that URL - her to-do list is still there

if __name__ == "__main__":
    unittest.main(warnings='ignore')

