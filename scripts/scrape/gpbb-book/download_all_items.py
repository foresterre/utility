#!/usr/bin/env python3

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import time
import math
import os

# ==============================================================================
#  From: https://stackoverflow.com/questions/3532979/python-how-to-download-a-zip-file
#  By: Gourneau
# ==============================================================================
#  License:  cc by-sa 3.0 (see From)
#  License page: https://creativecommons.org/licenses/by-sa/3.0/
# ==============================================================================
#  Adapted for Python 3 / compliance with PyLint.
# ==============================================================================

def download_in_chunks(url, to_dir):
    """Helper to download large files
        the only arg is a url
       this file will go to a temp DIRECTORY
       the file will also be downloaded
       in chunks and print out how much remains

       TODO: Change everything to Request (lib):
            response = requests.get(ANY_URL)
            response.headers['content-length']
    """
    print("Downloading file: ", url)

    base_file = os.path.basename(url)

    try:
        file = os.path.join(to_dir, base_file)

        req = urlopen(url)

        file_size = req.getheader('Content-Length')
        total_size = int(file_size)
        downloaded = 0
        chunk = 256 * 10240

        with open(file, 'wb') as file:
            while True:
                chunk = req.read(chunk)
                downloaded += len(chunk)
                if not chunk:
                    break
                progress_percentage = math.floor((downloaded / total_size) * 100)
                print("file: ", url, "| progress:", progress_percentage, "%")
                file.write(chunk)

    except HTTPError:
        print("HTTP Error!")
        return False
    except URLError:
        print("URL Error!")
        return False

    return file

# ==============================================================================
#  Downloads all Graphics Programming Black Book pdf's (plus source code)
#  to a folder called "gpbb" in the current directory.
# ==============================================================================
#  Script license:  The Unlicense or ISC License at your option.
#  The Unlicense copy: http://unlicense.org/
#  ISC License copy: https://opensource.org/licenses/ISC
# ==============================================================================
#  The Graphics Programming Black Book is © 2001 Michael Abrash 
# ==============================================================================

OTHER_PAGES = {
    "cover" : "http://downloads.gamedev.net/pdf/gpbb/gpbb.pdf",
    "toc" : "http://downloads.gamedev.net/pdf/gpbb/gpbb0.pdf",
    "intro" : "http://downloads.gamedev.net/pdf/gpbb/gpbbintr.pdf",
    "opening_page_1" : "http://downloads.gamedev.net/pdf/gpbb/gpbbpt1.pdf",
    "opening_page_2" : "http://downloads.gamedev.net/pdf/gpbb/gpbbpt2.pdf",
    "after_word" : "http://downloads.gamedev.net/pdf/gpbb/gpbbaftr.pdf"
}

SOURCE_CODE = "http://downloads.gamedev.net/zip/MichaelAbrashBlackBookSource.zip"

LINK = "http://downloads.gamedev.net/pdf/gpbb/"
CHAPTER_PREFIX = "gpbb"
LINK_AND_CHAPTER_PREFIX = "".join([LINK, CHAPTER_PREFIX])

def join_link(pre, mid: int, post):
    """
    Purpose of this helper routine is joining the LINK_AND_CHAPTER_PREFIX,
    the #n'th chapter number and the pdf extension together.
    The result is a link for each chapter.
    """
    return "".join([pre, str(mid), post])


if __name__ == '__main__':
    DIRECTORY = "gpbb" # file folder format: "{current_dir}/gpbb/{file}.pdf"
    SLEEP_SECONDS = 1
    FIRST_CHAPTER = 1
    LAST_CHAPTER = 70 + 1

    if not os.path.exists(DIRECTORY):
        os.mkdir(DIRECTORY)

    for i in range(FIRST_CHAPTER, LAST_CHAPTER):
        download_in_chunks(join_link(LINK_AND_CHAPTER_PREFIX, i, ".pdf"), DIRECTORY)
        time.sleep(SLEEP_SECONDS)

    for v in OTHER_PAGES.values():
        download_in_chunks(v, DIRECTORY)
        time.sleep(SLEEP_SECONDS)
        
    download_in_chunks(SOURCE_CODE, DIRECTORY)
