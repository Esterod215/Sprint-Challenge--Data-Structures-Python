class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    newest = 0
    oldest = 0
    if len(self.storage) < capacity:
      self.storage.append(item)
      newest = self.storage.index(item)
    else:
      self.storage[oldest] = value 
      newest = self.storage.index(value)
      if oldest + 1 > len(self.storage):
        oldest = newest
      else:
        oldest = oldest + 1
        

  def get(self):
    return self.storage


    