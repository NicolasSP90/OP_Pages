# Importing Libraries
import requests


def download_img(link, chapter_folder_path, index):
    response = requests.get(link)

    with open(f"{chapter_folder_path}{index}.jpg", "wb") as file:
        file.write(response.content)
        file.close()
