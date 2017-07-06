from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



class NewUserTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_user_table(self, row_text):
        table = self.browser.find_element_by_id('id_user_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


    def test_can_take_user_info_and_retrieve_it_later(self):
        ## Jamie has heard about a matchmaking app. She goes to its homepage
        self.browser.get('%s%s' % (self.live_server_url, '/user_registration/'))

        # She finds the page title and header mention matchmaking
        self.assertIn('Registration', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Registration', header_text)

        # She is immediately invited to answer a question and find a matchk
        # The question asks "What is your discipline?"
        inputbox = self.browser.find_element_by_id('id_discipline')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'User\'s discipline'
        )

        # She responds by typing in "Educator"
        inputbox.send_keys('Educator')

        # When she presses enter , the page updates to show
        # her discipline at the top of the page
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)


        # Another question has appeared, asking Jamie "Name a friend's
        # discipline."
        inputbox = self.browser.find_element_by_id('id_discipline')
        # She types in "The Rolling Stones" and presses enter
        inputbox.send_keys('Engineer')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page now shows her field of interest, as well as her favorite artist
        self.check_for_row_in_user_table('Discipline 1: Educator')
        self.check_for_row_in_user_table('Discipline 2: Engineer')

        # Finally, Jamie is asked to name her favorite sports
        # She enters Baseball
        self.fail('Finish the test!')

        # The page proudly displays 3/3 questions completed and shows
        # another user that shares some answers with her.

        # A button invites her to send a message to the user.
        # As its late, she declines, intending to explore the option later.

        # While wondering if the website would save her answers, Jamie
        # notices the page has generaated a unique URL and displayed it for her

        # She visits the url, her user profile is still there

        # Satisfied, she goes to watch television.
