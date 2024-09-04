class Vector:
  def __init__(self):
    self.capacity = 16
    self.size = 0
    self.data = [None] * self.capacity

  def get_size(self):
    return self.size
  
  def get_capacity(self):
    return self.capacity
  
  def is_empty(self):
    if self.size == 0:
      return True
    else:
      return False

  def at(self, index):
    if (index > self.capacity - 1):
      raise Exception('Index out of bounds')
    else:
      return self.data[index]