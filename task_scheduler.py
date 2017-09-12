"""
implement a scheduler service with schedule(Runnable task, Time timeInTheFuture) 
method, there will be many callers to call this method to ask the service to run 
tasks at given times in the future, the service need to make sure to run these 
tasks at required times, consider concurrency, memory efficiency etc, what if 
the requested time is in millisecond precision, what if the time is in 
microsecond/nanosecond precision
"""



class Task(Thread):
  def __init__(self, callback):
    Thread.__init__(self)
    self._callback = callback

  def run(self):
    self._callback()



class Executor(Thread):

  def __init__(self, task_queue, task_queue_cv):
    Thread.__init__(self)
    self._task_queue = task_queue
    self._task_queue_cv = task_queue_cv

  def run(self):
    while True:
      with self._task_queue_cv:
        task_threads = []
        while not self._task_queue.empty():
          execution_time, task = self._task_queue.get()
          if execution_time > time():
            self._task_queue.put((execution_time, task))
            break

          task.start()
          task_threads.append(task)

        for task_thread in task_threads:
          task_thread.join()



class Scheduler(Thread):

  def __init__(self, sleep_duration=1):
    Thread.__init__(self)
    self._task_queue = PriorityQueue()
    self._task_queue_cv = Condition()
    self._executor = Executor(self._task_queue, self._task_queue_cv)
    self._sleep_duration = sleep_duration

    self._executor.start()

  def run(self):
    while True:
      sleep(self._sleep_duration)
      with self._task_queue_cv:
        self._task_queue_cv.notify()

  def Schedule(self, task, start_time):
    self._task_queue.put((start_time, task))








from __future__ import print_function

from Queue import PriorityQueue
from threading import Condition
from threading import Thread
from time import sleep
from time import time


class Task(Thread):
  """Class to abstract a runnable task."""
  def __init__(self, callback):
    Thread.__init__(self)
    self._callback = callback

  def run(self):
    # Overrides the Therad.run method.
    self._callback()


class Executor(Thread):
  """Task executor class.

  This class is responsible for executing the task at the specified
  execution time. In a producer-consumer model, this is the consumer
  of tasks.
  """
  def __init__(self, task_queue, task_queue_cv):
    Thread.__init__(self)
    self._task_queue = task_queue
    self._task_queue_cv = task_queue_cv

  def run(self):
    """Start monitoring the task queue and execute tasks on demand."""
    while True:
      # We use an infinite loop here. This is because the executor can
      # be thought of as a "service", where the scheduler is the client.
      # Service in general never stops, until the process is killed.
      self._WaitAndProcessTasks()

  def _WaitAndProcessTasks(self):
    with self._task_queue_cv:
      while self._task_queue.empty():
        # Wait for scheduler to wake up executor, which happens
        # when the current timestamp surpasses head queue element's
        # execution timestamp.
        self._task_queue_cv.wait()

      task_threads = []
      while not self._task_queue.empty():
        execution_time, task = self._task_queue.get()
        if execution_time > time():
          # Still too early to run the task. Executor goes back
          # to sleep and put the task back to queue.
          self._task_queue.put((execution_time, task))
          break

        # Start executing the task in a separate thread.
        task.start()
        task_threads.append(task)

      # Wait for all scheduled tasks to finish.
      for task_thread in task_threads:
        task_thread.join()

      # Note that by the time all tasks a done, some tasks in the head
      # may now be available to run immediately. However, by design,
      # we do not allow for re-entrnace the tasks queue. The scheduler
      # class will notify this executor again to start executing these
      # tasks.


class Scheduler(Thread):
  """Class responsible for scheduling task and wake up executor thread.

  In a producer-consumer model, this can be though of as the producer of
  tasks.
  """
  def __init__(self, sleep_duration=1):
    Thread.__init__(self)
    self._task_queue = PriorityQueue()
    self._task_queue_cv = Condition()
    self._executor = Executor(self._task_queue, self._task_queue_cv)
    self._sleep_duration = sleep_duration

    # Kick-start the executor in a separate thread.
    self._executor.start()

  def run(self):
    while True:
      sleep(self._sleep_duration)
      with self._task_queue_cv:
        self._task_queue_cv.notify()

  def Schedule(self, task, start_time):
    # Register task in queue.
    self._task_queue.put((start_time, task))

#
# Example usage.
#

# Create the scheduler and start off in a separate thread.
scheduler = Scheduler()
scheduler.start()

# Create tasks and schedule them.
task1 = Task(lambda: print(1))
task2 = Task(lambda: print(2))
task3 = Task(lambda: print(3))
scheduler.Schedule(task1, time() + 1)
scheduler.Schedule(task2, time() + 2)
scheduler.Schedule(task3, time() + 3)

# Blocks until scheduler is done.
# Note that scheduler runs in an infinite loop, so the only way
# to exit is ctrl+c. This also means do not run this in Sublime!!!
scheduler.join()
