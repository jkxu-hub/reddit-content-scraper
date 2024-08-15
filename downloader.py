from urllib.request import urlopen, urlretrieve
import requests

def download_image(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urlretrieve(url, full_path)

url = "https://preview.redd.it/what-do-yall-think-of-my-tank-v0-w752mlzhbnxc1.jpeg?width=640&crop=smart&auto=webp&s=45c7fb65543622f9b0d2480dd4289c555d6ffec8"

filename = "img2"
download_image(url, 'images/', filename)

# response = urlopen(url2)
# print(response.info().get_content_type())

