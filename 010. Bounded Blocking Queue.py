from threading import Condition
from collections import deque
from threading import Lock
from threading import Thread


class BoundedBlockingQueue(object):
    def __init__(self, capacity):
        self.q = deque()
        self.capacity = capacity
        self.q_lock = Lock()
        self.full_cv = Condition()
        self.empty_cv = Condition()


    def enqueue(self, elem):
        with self.full_cv, self.q_lock:
            while len(self.q) == self.capacity:
                self.full_cv.wait()
            self.q.append(elem)

        with self.empty_cv, self.q_lock:
            if len(self.q) != 0:
                self.empty_cv.notifyAll()


    def dequeue(self):
        ret = None
        with self.empty_cv, self.q_lock:
            while len(self.q) == 0:
                self.empty_cv.wait()
            ret = self.q.popleft()

        with self.full_cv, self.q_lock:
            if len(self.q) < self.capacity:
                self.full_cv.notifyAll()
        return ret




class Task(Thread):
  def __init__(self, callback):
    Thread.__init__(self)
    self._callback = callback

  def run(self):
    self._callback()

bq = BoundedBlockingQueue(3)
puts = [Task(lambda: bq.enqueue(i)) for i in range(4)]
gets = [Task(lambda: bq.dequeue()) for i in range(2)]
tasks = puts + gets
for task in tasks:
    task.start()
for task in tasks:
    task.join()

print bq





from collections import deque
from threading import Condition
from threading import Lock
from threading import Thread


class BoundedBlockingQueue(object):
    def __init__(self, capacity):
        self.q = deque()
        self.capacity = capacity
        self.q_lock = Lock()
        self.full_cv = Condition()
        self.empty_cv = Condition()

        
    def __str__(self):
        return ','.join([str(elem) for elem in self.q])

    
    def enqueue(self, elem):
        with self.full_cv:
            with self.q_lock:
                q_size = len(self.q)
            while q_size == self.capacity:
                self.full_cv.wait()
                with self.q_lock:
                    q_size = len(self.q)
            self.q.append(elem)

        with self.empty_cv, self.q_lock:
            if len(self.q) != 0:
                self.empty_cv.notifyAll()


    def dequeue(self):
        ret = None
        with self.empty_cv:
            with self.q_lock:
                q_size = len(self.q)
            while q_size == 0:
                self.empty_cv.wait()
                with self.q_lock:
                    q_size = len(self.q)
            ret = self.q.popleft()

        with self.full_cv, self.q_lock:
            if len(self.q) < self.capacity:
                self.full_cv.notifyAll()

        return ret


class Task(Thread):
  def __init__(self, callback):
    Thread.__init__(self)
    self._callback = callback

  def run(self):
    self._callback()

bq = BoundedBlockingQueue(3)

puts = [
    Task(lambda: bq.enqueue(1)),
    Task(lambda: bq.enqueue(2)),
    Task(lambda: bq.enqueue(3)),
    Task(lambda: bq.enqueue(4)),
]

gets = [Task(lambda: bq.dequeue()) for i in range(2)]
for task in puts:
    task.start()
for task in gets:
    task.start()
for task in puts:
    task.join()
for task in gets:
    task.join()


print bq
