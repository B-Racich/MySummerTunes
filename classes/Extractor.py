import os.path
import youtube_dl
# from . import Logger

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

class Extractor:

  SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + '\Tracks'

  ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    # 'logger': Logger(),
    'download_archive': '/Tracks',
    'progress_hooks': [my_hook],
    'outtmpl':SAVE_PATH + '/%(title)s.%(ext)s',
  }

  def __init__(self):
    super().__init__()

  def download(self, url):
    with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
      print(ydl.extract_info(url))
      ydl.download([url])
    
    return 'yeet'
  
  