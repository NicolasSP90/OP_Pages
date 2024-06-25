# Importing Libraries
import requests
import os


def url_definition(urlbase, chapter):
    url = urlbase + chapter
    try:
        requests.get(url).raise_for_status()

    except requests.exceptions.HTTPError as error:
        print(error)
        os._exit(0)

    finally:
        return url
