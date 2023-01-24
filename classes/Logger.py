class MyLogger(object):
  def __init__(self):
    super().__init__()

  def debug(self, msg):
      pass

  def warning(self, msg):
      pass

  def error(self, msg):
      print(msg)