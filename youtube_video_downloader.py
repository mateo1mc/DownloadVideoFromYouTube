from pytube import YouTube
from pytube.cli import on_progress
import pytube.request
import random
import time
import os

pytube.request.default_range_size = 500000

def typewrite(num1, num2, text):
    for c in text:
        r = random.uniform(num1, num2)
        time.sleep(r)
        print(c, end='', flush=True)


def completed(stream):
    completed = '\nDownload Completed!\n'
    size = 'File Size: ' + str(stream.filesize / 1000000) + ' Mb\n'
    title = 'Title: ' + stream.title + '\n'
    author = 'Author: ' + yt.author + '\n'
    length = 'Video Length: ' + str(yt.length) + ' Seconds\n'

    txt_list = [completed, size, title, author, length]

    for t in txt_list:
        typewrite(.05, .1, t)
        print('-' * 60)


url = input("\nPlease enter the URL: ")
try:
    yt = YouTube(url, on_progress_callback=on_progress)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
    typewrite(.05, 1, 'Download is starting...\n')

    download_path = os.path.join(os.path.expanduser("~"), "Downloads")  # Path to the Downloads folder

    stream.download(output_path=download_path)
    completed(stream)
except Exception as e:
    print('Something Went Wrong! Please Try Again:', e)
