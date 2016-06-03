from time import time
import resource

class Counting():

    start_time = None

    def __enter__(self):
        self.start_time =  time()
        self.start_bytes = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    def __exit__(self, t, value, traceback):
        end_time =  time()
        end_bytes = self.start_bytes = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        diff_bytes = end_bytes - self.start_bytes
        duration = (end_time - self.start_time)
        print "> Duration: %.5fs" % duration
        print "> Memory: %s bytes" % end_bytes