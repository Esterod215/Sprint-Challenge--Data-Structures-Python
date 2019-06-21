class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    newest = 0
    if None in self.storage:
      newest = self.storage.index(None)
      self.storage[newest] = item

    else:
      self.storage[self.current] = item
      if self.current < self.capacity - 1:
        self.current += 1
      else:
        self.current = 0
        

  def get(self):
    return [index for index in self.storage if index != None]


arr = [2,6,8,9]
new_ring= RingBuffer(3)
new_ring.append(2)
new_ring.append(3)
new_ring.append(5)
new_ring.append(6)


print(new_ring.get())


