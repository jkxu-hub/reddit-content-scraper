# BS object creation errors:
# 1. server doesnt exist (incorrect URL) assertRaises(URLERROR)
# 2. page doesn't exist assertRaises(HTTPERROR)

# BS attribute errors:
# certain tags aren't found within the page
# maybe this shouldn't be handled by raising an exception, and should instead be handled with conditionals within a function?
# site html has changed


# test get_post_urls
# page contains many posts so you will have to scroll, does get_post_urls get all urls
# 

import unittest
from reddit_scraper import * 

class TestSoupCreation(unittest.TestCase):
    '''
        Beautiful soup object creation errors:
        # 1. server doesnt exist (incorrect URL) assertRaises(URLERROR)
        # 2. page doesn't exist assertRaises(HTTPERROR)
    '''
    def setUp(self):
        pass
    def test_server_not_found(self):
        url = 'https://www.reddsdfsdfdit.com/udfsdft/'
        encoding = 'utf-8'
        self.assertEqual(create_soup(url, encoding), None)
        
        
    def test_page_not_found(self):
        url_1 = 'https://www.reddit.com/user/Pink-plant/submittedsdfsd/'
        # url_2 = 'https://www.reddit.com/user/Pink-pla/'
        url_3 = 'https://www.reddit.com/udfsdft/'
        encoding = 'utf-8'
        self.assertEqual(create_soup(url_1, encoding), None)
        # self.assertEqual(create_bs_object(url_2, encoding), None)
        self.assertEqual(create_soup(url_3, encoding), None)
        
    def tearDown(self):
        pass



class TestNonExistentAttribute(unittest.TestCase):
    '''
        BS attribute errors:
        certain tags aren't found within the page
        maybe this shouldn't be handled by raising an exception, and should instead be handled with conditionals within a function?
        site html has changed
    '''
    def setUp(self):
        pass
    def test_attribute_not_found(self):
        pass
    def tearDown(self):
        pass


class Testget_post_urls(unittest.TestCase):
    '''
        # test get_post_urls
        # page contains many posts so you will have to scroll, does get_post_urls get all urls
    '''
    def setUp(self):
        pass
    def test_user_not_found(self):
        url = 'https://www.reddit.com/user/Pink-pla/'
        urls = get_post_urls(url)

        self.assertEqual(urls, None)
    
    # no scroll
    def test_normal_user(self):
        url = 'https://www.reddit.com/user/Pink-plant/'
        urls = get_post_urls(url)
        self.assertEqual(urls, None)
    
    # many posts (need to scroll with selenium)


    def tearDown(self):
        pass

class Testget_post_contents(unittest.TestCase):
    '''
        # test get_post_urls
        # page contains many posts so you will have to scroll, does get_post_urls get all urls
    '''

    # title doesn't exist
    # body doesn't exist
    # image doesn't exist
    # multiple photos in one post
    # Galleries: photos, gifs
    # external youtube
    # external imgur
    # external redgifs
    # poll
    # types accepted by reddit .png, .jpeg, .gif, .webp, .mp4, .mov

    def setUp(self):
        pass
    def test_user_not_found(self):
        url = 'https://www.reddit.com/user/hilarious0asdasdadw0/submitted/'
        urls = get_post_urls(url)

        self.assertEqual(urls, None)
    
    
    def test_normal_user(self):
        url = 'https://www.reddit.com/user/hilarious0w0/submitted/'
        # url = 'https://www.reddit.com/user/Pink-plant/submitted/'
        # url = 'https://www.reddit.com/user/JovaSilvercane13/submitted'
        urls = get_post_urls(url)
        print(len(urls))
        for url in urls:
            print(url)

        self.assertEqual(urls, None)
    
        
    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()