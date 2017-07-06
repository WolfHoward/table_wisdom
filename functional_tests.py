from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewUserTest(unittest.TestCase):

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
        self.browser.get('http://localhost:8000/user_registration/')

        # She finds the page title and header mention matchmaking
        self.assertIn('Registration', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Registration', header_text)

        # She is immediately invited to answer a question and find a matchk
        # The question asks "What is your discipline?"
        inputbox = self.browser.find_element_by_id('id_discipline')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter your discipline'
        )

        # She responds by typing in "Educator"
        inputbox.send_keys('Educator')

        # When she presses enter , the page updates to show
        # her discipline, in addition to "1/3 questions answered"
        # at the top of the page
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_user_table('Discipline: Educator')
        q_count = self.browser.find_element_by_id('id_q_count')
        print(q_count.text)
        self.assertEqual("1/3 Questions", q_count.text)
        # Another question has appeared, asking Jamie "Name your favorite
        # musical artist(s) [4 at most]".
        # inputbox = self.browser.find_element_by_id('id_discipline')
        # She types in "The Rolling Stones" and presses enter
        inputbox = self.browser.find_element_by_id('id_music_artist')
        inputbox.send_keys('Arctic Monkeys')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page now shows her field of interest, as well as her favorite artist
        self.check_for_row_in_user_table('Discipline: Educator')
        self.check_for_row_in_user_table('Favorite Musical Artists: Arctic Monkeys')

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

if __name__ == '__main__':
    unittest.main()
