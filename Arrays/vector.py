class Vector:
  def __init__(self):
    self.capacity = 16
    self.size = 0
    self.data = [None] * self.capacity

  def get_size(self):
    return self.size
  
  def get_capacity(self):
    return self.capacity
