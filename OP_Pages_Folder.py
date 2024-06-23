# Importing Libraries
import os


def folder_chapter(folder_path, chapter):
    full_path = os.path.join(folder_path, chapter)
    if not os.path.exists(full_path):
        os.makedirs(full_path)

    return full_path
