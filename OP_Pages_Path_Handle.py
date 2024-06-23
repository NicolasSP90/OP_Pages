# Importing Library
import os


def chapter_list():
    current_path = os.getcwd()
    chapter_folders_list = [chapters for chapters in os.listdir(current_path) if ".exe" not in chapters]
    chapter_folders_list.sort()

    return current_path, chapter_folders_list
