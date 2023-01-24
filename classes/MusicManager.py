import os.path
from classes.Extractor import Extractor

class MusicManager:

  metaPath = "/data/trackMetas.json"
  extractor = Extractor()

  def __init__(self):
    super().__init__()

  def download(self, url):
    return self.extractor.download(url)

