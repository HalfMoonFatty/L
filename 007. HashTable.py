"""Thread-safe hash table.
"""
from threading import Lock

class HashTable(object):
  def __init__(self, capacity):
    self.data = [[] for _ in range(capacity)]
    self.capacity = capacity
    self.size = 0
    self.lock = Lock()

  def __str__(self):
    return '\n'.join(str(bucket) for bucket in self.data)

  def _Rehash(self):
    # Double the size of the hash table ane rehashes all existing kv pairs.
    # Caller must hold table lock.
    self.capacity *= 2
    new_data = [[] for _ in range(self.capacity)]
    for bucket in self.data:
      for key, value in bucket:
        new_data[self._Hash(key)].append((key, value))
    self.data = new_data

  def _Hash(self, key):
    # Computes the hash value of the given key.
    return int(''.join([str(ord(c)) for c in str(key)])) % self.capacity

  def Put(self, key, value):
    # Stores the kv pair in hash table
    self.Remove(key)
    with self.lock:
      self.data[self._Hash(key)].append((key, value))
      self.size += 1
      if self.size == self.capacity:
        self._Rehash()

  def Get(self, key):
    # Gets the value for the given key. Raise KeyError if key is not found.
    with self.lock:
      bucket = self.data[self._Hash(key)]
      for k, v in bucket:
        if k == key:
          return v
      raise KeyError('Elememnt not found for key ' + str(key))

  def Remove(self, key):
    # Removes the kv pair for the given key. No-op if key is not found.
    with self.lock:
      bucket = self.data[self._Hash(key)]
      for i in range(len(bucket)):
        if bucket[i][0] == key:
          bucket.remove(bucket[i])
          self.size -= 1
          return

# Test cases.
ht = HashTable(5)
ht.Put(1, 'a')
ht.Put(2, 'b')
ht.Put(3, 'c')
ht.Put(4, 'd')
ht.Put(5, 'e')
ht.Put(6, 'f')
assert ht.Get(1) == 'a'
assert ht.Get(2) == 'b'
assert ht.Get(3) == 'c'
assert ht.Get(4) == 'd'
assert ht.Get(5) == 'e'
assert ht.Get(6) == 'f'
ht.Remove(4)
print ht
# ht.Get(7)  # <-- This shoud raise KeyError exception.
