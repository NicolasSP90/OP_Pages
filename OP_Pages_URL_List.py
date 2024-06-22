# importing libraries
from bs4 import BeautifulSoup
import re


def list_img_url(full_url, images_class):
    soup = BeautifulSoup(full_url, "html.parser")
    img_links = soup.find_all("img", {"class": re.compile(images_class)})

    # As Python List
    img_list = []
    for i in img_links:
        img_list.append(str(i))

    for i in range(0, len(img_list)):
        img_list[i] = img_list[i].split('src="')[1].split('"/>')[0].replace('amp;', '')

    return img_list
