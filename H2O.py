        
"""h2o lock everything"""

from threading import Condition

class H2O(object):
  def __init__(self):
    self.h = 0
    self.o = 0
    self.cv = Condtion()    

  def H(self):
    with self.cv:
      self.h += 1
      while self.h < 2 and self.o < 1:
        self.cv.wait()
      self.h -= 2
      self.o -= 1
      if self.h >= 2 and self.o >= 1:
        self.cv.notifyAll()

  def O(self):
    with self.cv:
      self.o += 1
      while self.h < 2 and self.o < 1:
        self.cv.wait()
      self.h -= 2
      self.o -= 1
      if self.h >= 2 and self.o >= 1:
        self.cv.notifyAll()

        
        
        
        


from threading import Condition

class H2O(object):

    def __init__(self):
        self.H = 0
        self.O = 0
        self.H_cv = Condition()
        self.O_cv = Condition()

    def H(self):
        # generate H element
        self.H_cv.acquire()
        self.H += 1
        if self.H >= 2:
            with self.O_cv:
                while self.O < 1:
                    self.H_cv.release()
                    self.O_cv.wait()
                    self.H_cv.acquire()
                if self.H >= 2 and self.O >= 1:
                    self.H -= 2
                    self.O -= 1
        self.H_cv.release()
        self.H_cv.notifyAll()



    def O(self):
        self.O_cv.acquire()
        self.O += 1
        with self.H_cv:
            while self.H < 2:
                self.O_cv.release()
                self.H_cv.wait()
                self.O_cv.acquire()
            if self.H >= 2 and self.O >= 1:
                self.H -= 2
                self.O -= 1
        self.O_cv.release()
        self.O_cv.notifyAll()


        
