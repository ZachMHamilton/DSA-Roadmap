class Vector:
  def __init__(self):
    self.capacity = 16
    self.size = 0
    self.data = [None] * self.capacity

  def getSize(self):
    return self.size
  
  
