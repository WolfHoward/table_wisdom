from selenium import webdriver
import unittest

class NewUserTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_take_user_info_and_retrieve_it_later(self):
        ## Jamie has heard about a matchmaking app. She goes to its homepage
        self.browser.get('http://localhost:8000')

        # She finds the page title and header mention matchmaking
        self.assertIn('User Registration', self.browser.title)
        self.fail('Finish the test!')

        # She is immediately invited to answer a question and find a matchk
        # The question asks "What is your field of study?"

        # She responds by typing in Educator

        # When she presses enter , the page updates to show
        # her field of study and the number of people that share that field,
        # in addition to "1/3 questions answered" at the top of the page

        # Another question has appeared, asking Jamie "Name your favorite
        # musical artist(s) [4 at most]".

        # She types in "The Rolling Stones" and presses enter

        # The page now shows her field of interest, as well as her favorite artist

        # Finally, Jamie is asked to name her favorite sports
        # She enters Baseball

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
