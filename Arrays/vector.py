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
    return self.size == 0

  def at(self, index):
    if (index > self.size):
      raise Exception('Index out of bounds')
    else:
      return self.data[index]
    
  def push(self, item):
    if self.size >= self.capacity:
      self.capacity *= 2
    self.data[self.size] = item
    self.size += 1