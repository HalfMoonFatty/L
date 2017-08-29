import time
import threading

class RateLimiter(object):
  def __init__(self, max_rps):
    self._max_rps = max_rps
    self._start_time = time.time()
    self._request_count = 0
    self._lock = threading.Lock()

  def Acquire(self):
    with self._lock:
      current_time = time.time()
      if current_time - self._start_time > 1:
        self._request_count = 1
        self._start_time = current_time
        return
      elif self._request_count < self._max_rps:
        self._request_count += 1
        return
      else:
        time.sleep(self._start_time + 1 - current_time)
        self._start_time = self._start_time + 1
        self._request_count = 1



class Printer(threading.Thread):
  def __init__(self, rate_limiter):
    threading.Thread.__init__(self)
    self._rate_limiter = rate_limiter

  def run(self):
    self._rate_limiter.Acquire()
    print 'hello!!!\n'

rate_limiter = RateLimiter(10)
printers = []
for i in range(100):
  p = Printer(rate_limiter)
  p.start()
  printers.append(p)

for p in printers:
  p.join()
