from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewQuizzTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_create_a_quizz_and_retrieve_it_later(self):
        # Luis has heard about a cool new online quizz app. 
        # He goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention Super Quizzes & New Quizz
        self.assertIn('Super Quizzes', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('New Quizz', header_text)

        # He is invited to enter a quizz title item straight away
        inputbox = self.browser.find_element_by_id('id_quizz_title')  
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Quizz Title'
        )

        # He types "Python Test 1" into a text box
        # (Luis is a python instructor)
        inputbox.send_keys('Python Test 1')

        # When he hits enter, the page updates, and now the page lists
        # "Python Test 1" as a caption in a quizz table
        inputbox.send_keys(Keys.ENTER)  
        time.sleep(1)  

        table = self.browser.find_element_by_id('id_quizz_table')
        caption = table.find_element_by_tag_name('caption')
        self.assertTrue(caption.text == 'Python Test 1')
        #self.fail('Finish the Test')

if __name__ == '__main__':
    unittest.main()