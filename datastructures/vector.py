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
    if index > self.size:
      raise Exception('Index out of bounds')
    else:
      return self.data[index]
    
  def push(self, item):
    self.__resize(self.size + 1)
    self.data[self.size] = item
    self.size += 1

  def insert(self, item, index):
    if index > self.size:
      raise Exception('Index out of bounds')
    self.__resize(self.size + 1)
    for i in range(self.size - 1, index - 1, -1):
      self.data[i + 1] = self.data[i]
    self.data[index] = item
    self.size += 1

  def prepend(self, item):
    self.__resize(self.size + 1)
    for i in range(self.size - 1, 1, -1):
      self.data[i + 1] = self.data[i]
    self.data[0] = item
    self.size += 1
      
  def pop(self):
    if self.size == 0:
      raise Exception('Array is empty')
    item = self.data[self.size - 1]
    self.size -= 1
    self.__resize(self.size)
    self.data[self.size] = None
    return item
  
  def delete(self, index):
    if index > self.size - 1:
      raise Exception('Index out of bounds')
    for i in range(index, self.size - 1):
      self.data[i] = self.data[i + 1]
    self.data[self.size - 1] = None
    self.size -= 1
    self.__resize(self.size)

  def remove(self, item):
    for i in range(self.size):
      if self.data[i] == item:
        for j in range(i, self.size - 1):
          self.data[j] = self.data[j + 1]
        self.size -= 1
        self.data[self.size] = None
        self.__resize(self.size)
        return
    raise Exception('Item not found')    
    
  def find(self, item):
    for i in range(self.size):
      if self.data[i] == item:
        return i
    return -1
  
  def __resize(self, new_size):
    new_capacity = self.capacity

    if (new_size > self.capacity):
      new_capacity = self.capacity * 2
    elif new_size >= 16 and new_size <= self.capacity // 4:
      new_capacity = self.capacity // 2

    new_data = [None] * new_capacity

    for i in range(self.size):
        new_data[i] = self.data[i]
  
    self.data = new_data
    self.capacity = new_capacity

