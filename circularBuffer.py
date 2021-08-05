class CircularQueue:
  
  def __init__(self, maxSize):
    self.queue = list()
    # kullanıcı girdisi üzerine maxBoyut
    self.maxSize = maxSize
    self.head = 0
    self.tail = 0

  # Eleman ekleme
  def enqueue(self, data):
    # BufferDolu mu(Kuyruk) kontrolü
    if self.size() == (self.maxSize - 1):
      return("Buffer(Queue) is full!")
    else:
      # Eleman ekleme
      self.queue.append(data)
      # indexi artırma işlemi
      self.tail = (self.tail+1) % self.maxSize
      return True
  
  # Eleman çıkarma
  def dequeue(self):
    # BufferBoş mu(Kuyruk) kontrolü
    if self.size() == 0:
      return("Buffer(Queue) is empty!")
    else:
      # Buffer içindeki veriler.
      data = self.queue[self.head]
      # Head artır geriye hareket.
      self.head = (self.head+1) % self.maxSize
      return data
  
  # Buffer'ın boyutu
  def size(self):
    if self.tail >= self.head:
      qSize = self.tail - self.head
    else:
      qSize = self.maxSize - (self.head - self.tail)
    return qSize

# kullanıcı boyut girdisi
size = input("Enter the size of the Circular Buffer(Queue)")
q = CircularQueue(int(size))
print(q.enqueue(10))
print(q.enqueue(20))
print(q.enqueue(30))
print(q.enqueue(40))
print(q.enqueue(50))
print(q.enqueue('Çıkarıp Eklenen'))
print(q.enqueue(70))
print(q.enqueue(80))
print(q.dequeue())
print(q.dequeue())