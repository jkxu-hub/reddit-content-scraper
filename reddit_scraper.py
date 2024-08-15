from urllib.request import urlopen, Request, urlretrieve
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
from selenium import webdriver 
import os
import re 
import time

'''
todo:
- error handling on getting post contents: what if video, post body, title, etc. is missing
- error handling on all possible scenarios where user input/website scrape input could be incorrect
- write tests for the functions
- figure out how you want to store a users content: csv or database?
- create function that will download all video/image links from the database
- scroll capability so you can get all of a user's post quickly

'''
# Checks that an object was successfully created
def valid_object(object):
     if object == None:
          return False
     else:
          return True
     
def create_soup(reg_url: str, encoding: str) -> BeautifulSoup:
        '''
        Creates a Get Request that contains a user agent header, so that the browser doesn't
        detect we are a bot. Checks for HTTPError (page is not found by website server). Checks for URLError (website server is down or not found).
        
        :param reg_url: the normal url we are trying to scrape
        :param encoding: the encoding type

        :return A beutiful soup object representing the html sent from server for the specified reg_url
        '''

        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', 
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'}
        
        # creates a request object that will be passed to urlopen
        req = Request(url = reg_url, headers = headers)

        # gets the html associated with the req
        try:
          html = urlopen(req)
        except HTTPError as e:
          # print(e.code)
          return None
        except URLError as e:
          # print("Server not found", e)
          return None
        else:

          return BeautifulSoup(html.read(), 'html5lib', from_encoding=encoding)
     
def user_not_found(soup: BeautifulSoup) -> bool:
    # print(bs.find("shreddit-forbidden"))
    # print("hello")
    return not (soup.find("shreddit-forbidden") == None)
    # return not bs.shreddit-forbidden == None
    

# Takes in the page of a user and returns the urls to the posts for that user
#
# TODO the html needs to be fully loaded on the page
#
# post_page_url is the url to the post page of a redditor
def get_post_urls(profile_page_url: str) -> list:
     # TODO verify that it is a valid user's URL

     soup = create_soup(profile_page_url, 'utf-8')
     if not valid_object(soup):
          print("Failed to get user at: " + profile_page_url)
          return None 
     
     if user_not_found(soup):
         print("Failed to get user at: " + profile_page_url + " account may have been banned.")
         return None

     
     # if the soup object contains the forbidden tag shreddit-forbidden
     # print user not found or may have been banned
     post_urls = []
     for a_tag in soup.find_all(slot="full-post-link"):
          link = "https://www.reddit.com" + a_tag.get('href')
          post_urls.append(link)

     return post_urls

# a function that takes in the posts of a user and returns the title, body, image/videos/gifs, and the associated subreddit
#
# possible errors: title doesn't exist, body doesn't exist, image doesn't exist, videos/gifs don't exist, etc., multiple photo uploads for one page, should you download other content type?, random other files
def get_post_contents(post_page_url: str):
    soup = create_soup(post_page_url, 'utf-8')
    if not valid_object(soup): 
         print("Failed to get post at: " + post_page_url)
    
    # check if attributes are found

    # title: check if these things can be found
    title = soup.find('h1').text.strip() # TODO is there any way we don't need to strip here?
    # print(title)
    # body
    body = soup.find('div', slot = 'text-body').find('p').text.strip()  
    # print(body)

    # image
    image = soup.find('img', id = 'post-image')['src']
    # print(image)





'''
redditor_link = 'https://www.reddit.com/user/Pink-plant/submitted/'

post_urls = get_post_urls(redditor_link)
# get_post_contents(post_urls[1])

for post_url in post_urls:
     get_post_contents(post_url)
     
'''




# redditor_link = 'https://www.reddit.com/user/Pink-plant/submittedsadasda/'
# create_soup(redditor_link, 'utf-8')

