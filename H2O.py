


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
